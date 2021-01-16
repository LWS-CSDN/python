'''
https://blog.csdn.net/weixin_33797791/article/details/88727361
https://blog.csdn.net/sinat_38682860/article/details/108754245
1 .通过队列Queue来实现。主线程启动一个线程来读文件，把文件的内容放到队列里。
然后启动若干线程，全部从队列取数据。python中的Queue是线程安全的。
http://stackoverflow.com/questions/18781354/is-iterating-over-a-python-file-object-thread-safe

2. 通过linecache来实现。linecache可以指定行号来读取一个文件的任意一行。主线程先分配给每个读线程各自读取的行号，然后各线程根据行号用linecache来读取。
此种方法依赖于linecache读取任意一行的速度，如果是大文件，则比较慢。
比如线程1需要读取10-20行。假设线程1有自己的文件指针的话，读了地10行，可以直接很快定位到第11行。但是用linecache读取的话，每一次读取一行就没有什么关系了。当然，对于linecache怎么定位到任意一行，其中的原理我也没探究过。

3.分文件读取。python先调用linux命令head和tail，将一个文件分成若干个文件。然后每个读线程负责读取一个文件即可。


1.打开文件的数据,然后存到变量里,然后多线程进行增删改查,等到多线程都执行一遍,然后再把变量的数据写入到文件中
2.打开文件的数据,多线程谁先执行完,谁就先增删改查加锁,前一个线程如果3秒没有执行完毕,自动跳过继续下一个线程读写
缺点:一个线程增删改查,影响其他线程,速度慢
3.用读写锁和2很像,但是比2要优化很多,读写锁也有分读优先和写优先,防止一直读或者一直写,如果读的话,多线程大家一起读
读的优先级高:一直读,想写的数据一直没有写入
写的优先级高:一直写,想读的数据读不了
只读,只写,读完再写,写完再读
多个线程先读后写锁容易造成死锁:因为1号线程读完要写,2号在等1号写锁释放再读


需要了解的概念
1.可重入锁。 可重入锁是指同一个锁可以多次被同一线程加锁而不会死锁。 实现可重入锁的目的是防止递归函数内的加锁行为，或者某些场景内无法获取锁A是否已经被加锁，这时如果不使用可重入锁就会对同一锁多次重复加锁，导致立即死锁。
2.读写锁。 读写锁与一般锁最大的区别是对同一共享资源多个线程的读取行为是并行的，同时保持该资源同一时刻只能由一个写进程独占，且写请求相对读请求有更高的优先级以防止writer starvation。( 一般锁同一时刻只能由一个线程独占，不论是读进程还是写进程， 即读写都是串行的，而读写锁读是并行的，写是串行的。)
读写锁的特点是：
2.1 当且仅当 锁没有被写进程占用且没有写请求时，可以获得读权限锁
2.2 当且仅当 锁没有被占用且没有读写请求时，可以获得写权限锁
读写锁的状态自动机可以参考下图
rwlock_dfa
所有数据库都拥有读写锁，当必要时，会自动将读锁提升为写锁，称为lock promotion。
1.慎用promote ! 读写锁一般都有提权函数promote()用于将一个已经获取读锁的线程进一步提权获得写锁，
这样做很容易导致程序死锁。例如，两个均已经获取读锁的线程A和B同时调用promote函数尝试获得写权限，
线程A发现存在读线程B，需要等待B完成以获取写锁，线程B发现存在读线程A，需要等待线程A完成以获取写锁，
循环等待发生，程序死锁。因此，当且仅当你能确定当前仅有一个读线程占有锁时才能调用promote函数。
一个已经获取读锁的线程提权最好的办法是先释放读锁，然后重新申请写锁。

2.使用多个锁时保证加解锁顺序相反。 考虑以下错误代码：
A.lock();
B.lock();
Foo();
A.unlock();
Bar();
B.unlock();

3.如果在Bar函数中尝试重新获取锁A，那么获取B锁之前先要获取A锁的语义就被破坏了，因为你尝试在拥有锁B的情况下获取锁A，而不是意图实现的相反情况，并且Bar函数在A锁的关键区之外，该实现有可能导致死锁或其它未定义的情况。
正确的实现应该是按照C++中的RAII原则加解锁， 在python中使用with语法
lockA=threading.lock()
lockB=threading.lock()
with lockA:
  with lockB:
    Foo();
  Bar()

4.
读写锁目前的非官方实现
下列为目前发现的python rwlock的非官方实现
1. https://majid.info/blog/a-reader-writer-lock-for-python/
2. https://hdknr.github.io/docs/django/modules/django/utils/synch.html#RWLock
3. https://code.activestate.com/recipes/577803-reader-writer-lock-with-priority-for-writers/
4. https://github.com/azraelxyz/rwlock/blob/master/rwlock/rwlock.py

5.存在的问题
由于4个实现全部贴出代码内容较长，因此这里略去。推荐阅读[1]和[4]的实现。
1.  [1]. 使用条件变量实现，
    [2]. 使用信号量实现，实际效果没有区别（信号量类有内部计数器，既可以当锁又可以当条件变量）,但在当前需求下使用条件变量的版本更通俗易懂且[2]. 没有测试代码。
    [3]. 中测试代码最全且使用了unittest，但自己实现的信号量_LightSwitch的auquire和release语义和python threading库正好相反，不推荐。
    [4]. 的实现最规范也最复杂，已经提交给了issue8800, 与其它3个实现的主要区别是自己实现了可重入锁, 但是没有promote和demote接口也没有测试代码。
2. 除了[2]和[4]，其它两个个版本的锁都是不可重入的。
通过分析4个版本的源码可以看出，4个版本[1]的实现最均衡，唯一实现了promote和demote函数,代码也最清晰易懂，
但是4个版本均存在无法完全解决writer starvation的问题(没有队列保证公平性，随机唤醒写线程，如果写线程较多可能会出现某一阻塞等待的写线程永远无法被唤醒的情况 )。

6.改进版的读写锁实现
针对[1]的改进主要包括两点：
1. 增加了写请求队列(python中threading.Queue是线程安全的), 唤醒写线程时按照FIFO实现公平调度，避免大量写进程等待时可能发生的writer starvation
2. 将threading.lock改为可重入的threading.Rlock
3. 如果对同时并发读取的线程数有限制，则可以在RWLock的构造函数__init__中定义一个最大同时读取数max_reader_num，同时将acquire_read中的条件判断替换为:
while self.rwlock < 0 or self.rwlock == max_reader_num or self.writers_waiting:

即可实现限制并发读取的最大线程数。

改进的实现代码
扩展阅读
spin-lock使用while循环的目的是解决spurious wakeup
使用信号量的目的是解决missed signal
参考文献
http://tutorials.jenkov.com/java-concurrency/read-write-locks.html
'''
import threading

from queue import Queue


class RWLock:
    """
    A simple reader-writer lock Several readers can hold the lock
    simultaneously, XOR one writer. Write locks have priority over reads to
    prevent write starvation. wake up writer accords to FIFO
    一个简单的读取器-写入器锁几个读取器可以持有该锁
    同时，异或一个作家。写锁的优先级高于读锁
    防止写饥饿。觉醒的作家同意FIFO
    """

    def __init__(self):
        '''
        self.wait_writers_q初始化队列
        self.monitor多重锁 
        在同一线程中可用被多次acquire。如果使用RLock，那么acquire和release必须成对出现，
        调用了n次acquire锁请求，则必须调用n次的release才能在线程中释放锁对象
        '''
        self.wait_writers_q = Queue()
        self.rwlock = 0
        self.writers_waiting = 0
        self.monitor = threading.RLock()
        self.readers_ok = threading.Condition(self.monitor)

    def acquire_read(self):
        """Acquire a read lock. Several threads can hold this typeof lock.
        It is exclusive with write locks."""
        self.monitor.acquire()
        while self.rwlock < 0 or self.writers_waiting:
            self.readers_ok.wait()
        self.rwlock += 1
        self.monitor.release()

    def acquire_write(self):
        """Acquire a write lock. Only one thread can hold this lock, and
        only when no read locks are also held."""
        self.monitor.acquire()
        while self.rwlock != 0:
            self.writers_waiting += 1
            writers_ok = threading.Condition(self.monitor)
            self.wait_writers_q.put(writers_ok)
            writers_ok.wait()
            self.writers_waiting -= 1
        self.rwlock = -1
        self.monitor.release()

    def promote(self):
        """Promote an already-acquired read lock to a write lock
        WARNING: it is very easy to deadlock with this method"""
        self.monitor.acquire()
        self.rwlock -= 1
        while self.rwlock != 0:
            self.writers_waiting += 1
            writers_ok = threading.Condition(self.monitor)
            self.wait_writers_q.put(writers_ok)
            writers_ok.wait()
            self.writers_waiting -= 1
        self.rwlock = -1
        self.monitor.release()

    def demote(self):
        """Demote an already-acquired write lock to a read lock"""
        self.monitor.acquire()
        self.rwlock = 1
        self.readers_ok.notifyAll()
        self.monitor.release()

    def release(self):
        """Release a lock, whether read or write."""
        self.monitor.acquire()
        if self.rwlock < 0:
            self.rwlock = 0
        else:
            self.rwlock -= 1
        wake_writers = self.writers_waiting and self.rwlock == 0
        wake_readers = self.writers_waiting == 0
        self.monitor.release()
        if wake_writers:
            # print "wake write..."
            writers_ok = self.wait_writers_q.get_nowait()
            writers_ok.acquire()
            writers_ok.notify()
            writers_ok.release()
        elif wake_readers:
            self.readers_ok.acquire()
            self.readers_ok.notifyAll()
            self.readers_ok.release()

    def que(self):
        while True:
            print("当前队列大小:",self.wait_writers_q.qsize())
            time.sleep(1)

if __name__ == '__main__':
    import time
    rwl = RWLock()
    threading.Thread(target=rwl.que).start()
    class Reader(threading.Thread):
        def run(self):
            print(self, 'start')
            rwl.acquire_read()
            print(self, 'acquired')
            time.sleep(5)
            print(self, 'stop')
            rwl.release()

    class Writer(threading.Thread):
        def run(self):
            print(self, 'start')
            rwl.acquire_write()
            print(self, 'acquired')
            time.sleep(10)
            print(self, 'stop')
            rwl.release()
            rwl.release()

    class ReaderWriter(threading.Thread):
        def run(self):
            print(self, 'start')
            rwl.acquire_read()
            print(self, 'acquired')
            time.sleep(5)
            rwl.promote()
            print(self, 'promoted')
            time.sleep(5)
            print(self, 'stop')
            rwl.release()

    class WriterReader(threading.Thread):
        def run(self):
            print(self, 'start')
            rwl.acquire_write()
            print(self, 'acquired')
            time.sleep(10)
            print(self, 'demoted')
            rwl.demote()
            time.sleep(10)
            print(self, 'stop')
            rwl.release()

    Reader().start()
    time.sleep(1)
    Reader().start()
    time.sleep(1)
    ReaderWriter().start()
    time.sleep(1)
    WriterReader().start()
    time.sleep(1)
    Reader().start()
    for i in range(5):
        time.sleep(1)
        Writer().start()

    
# #! /usr/bin/env python
# # coding=utf-8

# from threading import Thread
# import threading
# import time
# from ltz_schedule_times import *

# # 1、不加锁


# def lock_test():
#     time.sleep(0.1)
#     schedule_times = ReadTimes()
#     print(schedule_times)
#     schedule_times = schedule_times + 1
#     WriteTimes(schedule_times)


# if __name__ == '__main__':

#     for i in range(5):
#         Thread(target=lock_test, args=()).start()
