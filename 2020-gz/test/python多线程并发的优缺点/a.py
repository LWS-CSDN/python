'''
并发的优点：
要把100M 数据写入磁盘，CPU 计算的时间只需要0.01s，可是磁盘接受这100M 数据却需要10s，
怎么办呢？有两种办法
1、第一种办法是 CPU 等着，也就是程序暂停执行后续代码，直到磁盘写入数据完成再继续往下执行
适合实时性数据
'''
#import  threading
# import time
# start_time=time.time()
# def foo(str):
#     print(str)
#     time.sleep(2)


# foo('磁盘接受100M数据')
# foo('数据接受完毕，cpu去做其他事情。')
# end_time=time.time()
# times= end_time-start_time
# print('共使用时间：',times)

'''
2、第二种办法是 CPU 告诉磁盘：“您老人家慢慢写，我去做别的事情了”
很适合爬虫
'''
# import time
#import  threading
# start_time=time.time()
# def foo(str):
#     print(str)
#     time.sleep(2)

# t1=threading.Thread(target=foo,args=('磁盘接受100M数据',))
# t2=threading.Thread(target=foo,args=('你慢慢写，cpu去做其他事情',))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end_time=time.time()
# times= end_time-start_time
# print('共使用时间：',times)

'''
3.虚拟DOM的两种创建方式.注意：多线程对I/O 有效果，对于需要cpu计算的 时候，反复切换会浪费时间反而会降低效率具体看下面的例子：
看下面的并行的代码
'''
# import time,threading
# begin_time=time.time()
# def foo1():
#     _sum=0
#     for i in range(5000000):
#         _sum+=1

#     print(_sum)
# foo1()
# foo1()
# end_time=time.time()
# times=end_time-begin_time
# print(times)

'''
4.看下面并发多线程执行的代码
'''
# import time,threading
# begin_time=time.time()
# def foo1():
#     _sum=0
#     for i in range(5000000):
#         _sum+=1

#     print(_sum)
# t1=threading.Thread(target=foo1)
# t2=threading.Thread(target=foo1)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end_time=time.time()
# times=end_time-begin_time
# print(times)
'''
小明有一张银行卡余额500元,这张银行卡绑定小明妻子的微信和支付宝手中.
小明今天发工资了,收入人民币10000元,在银行汇款的同时小明的妻子通过支付宝消费口红一支300元
-两件事都需要操作一个变量-->账户余额
-两件事几乎同时发生,所以同时取到余额这个变量balance,都是500元
-线程A计算工资收入:500+10000=10500元 banlance=10500
-线程B计算消费支出:500-300=200元 banlance=200
-显然,并发操作数据是不安全的

5.多个线程都在同时操作同一个共享资源，所以造成了资源破坏，怎么办呢？
有同学会想用 join 呗，但 join 会把整个线程给停住，造成了串行，失去了多线程的意
义，而我们只需要把计算(涉及到操作公共数据)的时候串行执行。
我们可以通过 同步锁 来解决这种问题
'''
# import threading ,time,random
# account_balance=500
# alock=threading.Lock()
# def foo1(num):
#     alock.acquire()
#     global account_balance
#     balance=account_balance
#     balance+=num
#     time.sleep(random.randint(0,10)*0.01)#数据操作耗时不确定
#     account_balance=balance
#     alock.release()
#     # time.sleep(2)

# t1=threading.Thread(target=foo1,args=(-300,))
# t2=threading.Thread(target=foo1,args=(100000,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('银行卡结余工资：',account_balance)
'''
6.下面我们在说说，死锁和递归锁
'''
# import threading,time
# lockR=threading.RLock()

# def foo1():
#     lockR.acquire()
#     print('a1上锁')
#     lockR.acquire()
#     print('b1已上锁')
#     lockR.release()
#     print('b1已解锁')
#     lockR.release()
#     print('a1已解锁')

# def foo2():
#     lockR.acquire()
#     print('b2已上锁')
#     lockR.acquire()
#     print('a2已上锁')
#     lockR.release()
#     print('a2已解锁')
#     lockR.release()
#     print('b2已解锁')

# t1=threading.Thread(target=foo1)
# t2=threading.Thread(target=foo2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('主线程已执行完毕')
'''
7.条件的变量同步
有一个线程需要等待某个条件才会执行，比如某几条测试用例必须在完成一个初始化之后才能执行；
比如早点铺子的师傅必须蒸好包子，客人才能把包子买来吃掉
python 提供了threading.Condition 对象用于条件线程的支持
他除了能提供Rlock()或者 Lock()的方法之外，还提供了wait() 、notify()、notifyAll() 方法
'''
# import time, threading ,random
# loc_con=threading.Condition()
# num_list=[]
# def producer():
#     global num_list
#     while True:
#         if  loc_con.acquire():
#             num_list.append(1)
#             print('做好了一个包子现在盘子里有包子',num_list)
#             loc_con.notify()
#             loc_con.release()
#             time.sleep(random.randint(0,10)*0.1)

# def customer():
#     global num_list
#     while True:
#         if loc_con.acquire():
#             if len(num_list)==0:
#                 print('没有包子等一会')
#                 loc_con.wait()
#             num_list.remove(num_list[0])
#             print('消费者吃掉了一个包子',num_list)
#             loc_con.notifyAll()
#             loc_con.release()
#             time.sleep(random.randint(0,10)*0.4)
# t1=threading.Thread(target=producer)
# t2=threading.Thread(target=customer)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
'''
8.多线程中的 信号量
信号量是用来控制线程并发数的，BoundeSemaphore或Semaphore 管理一个内置的计数器，每当调用acquire() 时 -1 ，
 调用release（）时+1计数器不能小于0，当计数器为0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release（）
BoundeSemaphore 与 Semaphore 的唯一区别在与在前者调用release()时检查计数器的值师傅超过了计数器的初始值，如果超过了将会抛一个异常
'''
import threading ,time
bs=threading.BoundedSemaphore(5)
def  foo(num):
    bs.acquire()
    print('我车子停在：%d  号车位'%num)
    time.sleep(1)
    bs.release()
    print('我停在：%d  号车位的车子被开走了'%num)


for i in range(1,10):
    t1=threading.Thread(target=foo,args=(i,))
    t1.start()

