

#! /usr/bin/env python
# coding=utf-8

from threading import Thread
import threading
import time
from ltz_schedule_times import *

# 2、加锁
mu = threading.Lock()  # 1、创建一个锁


def lock_test():
    # time.sleep(0.1)
    if mu.acquire(True):  # 2、获取锁状态，一个线程有锁时，别的线程只能在外面等着
        schedule_times = ReadTimes()
        print schedule_times
        schedule_times = schedule_times + 1
        WriteTimes(schedule_times)
        mu.release()  # 3、释放锁


if __name__ == '__main__':

    for i in range(5):
        Thread(target=lock_test, args=()).start()
