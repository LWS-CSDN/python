import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            msg='我是'+self.name+str(i)
            print(msg)
            

if __name__=='__main__':
    t=MyThread()
    t.start()