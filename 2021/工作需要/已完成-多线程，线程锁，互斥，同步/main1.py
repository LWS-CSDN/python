import time
import threading
'''
同步
'''
NUM=0
#创建一把锁,锁是开的
mutex=threading.Lock()
class MyThread(threading.Thread):
    def run(self):
        global NUM
        mutexFlage=mutex.acquire()
        print('线程(%s)的锁状态为%d'%(self.name,mutexFlage))
        #判断上锁是否成功
        if mutexFlage:
            NUM=NUM+1
            time.sleep(1)
            msg=self.name+'set num to'+str(NUM)
            print(msg)
            #解锁
            mutex.release()
def test():
    for i in range(5):
        t=MyThread()
        t.start()

if __name__=='__main__':
    test()