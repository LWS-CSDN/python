#!/usr/bin/env python3
""" Several users reading a calender, but only a few users updating it """

import threading
import time

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0
marker = threading.Lock()

def calendar_reader(id_number):
    global today
    name = 'Reader-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        marker.acquire()
        print(name, 'sees that today is', WEEKDAYS[today])
        marker.release()

def calender_writer(id_number):
    global today
    name = 'Write-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        marker.acquire()
        today = (today + 1) % 7
        print(name, 'updated date to ', WEEKDAYS[today])
        marker.release()

if __name__ == '__main__':
    #  create ten reader threads
    begin_time=time.time()
    for i in range(10):
        threading.Thread(target=calendar_reader, args=(i,)).start()
    #  ...but only two writer threads
    for i in range(2):
        threading.Thread(target=calender_writer, args=(i,)).start()
  
    end_time=time.time()
    times=end_time-begin_time
    print("用时:",times,"秒")
    