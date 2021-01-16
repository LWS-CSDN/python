'''
1.无锁
结果显示混乱
'''
#coding=utf8
# import threading
# import time

# num = 0

# def sum_num(i):
#     global num
#     time.sleep(1)
#     num +=i
#     print(num)

# print('%s thread start!'%(time.ctime()))

# try:
#    for i in range(6):
#        t =threading.Thread(target=sum_num,args=(i,))
#        t.start()
# except KeyboardInterrupt:
#     print("you stop the threading")

# print('%s thread end!'%(time.ctime()))

'''
2.引入锁
数据显示正常
'''
#coding=utf8
import threading
import time

num = 0

def sum_num(i):
    start_time=time.time()
    lock.acquire()
    global num
    time.sleep(1)
    num +=i
    print(num)
    lock.release()

print('%s thread start!'%(time.ctime()))

try:
   lock=threading.Lock()
   list = []
   for i in range(6):
       t =threading.Thread(target=sum_num,args=(i,))
       list.append(t)
       t.start()

   for threadinglist in list:
        threadinglist.join()

except KeyboardInterrupt:
    print("you stop the threading")

print('%s thread end!'%(time.ctime()))
'''
3.引入多重锁
'''
#coding=utf8
# import threading
# import time

# num = 0

# def sum_num(i):
#     lock.acquire()
#     global num
#     lock.acquire()
#     time.sleep(1)
#     num +=i
#     lock.release()
#     print(num)
#     lock.release()

# print('%s thread start!'%(time.ctime()))

# try:
#    lock=threading.RLock()
#    list = []
#    for i in range(6):
#        t =threading.Thread(target=sum_num,args=(i,))
#        list.append(t)
#        t.start()

#    for threadinglist in list:
#         threadinglist.join()

# except KeyboardInterrupt:
#     print("you stop the threading")

# print('%s thread end!'%(time.ctime()))



