#!/usr/bin/python
#coding=utf-8
'''
shutil
文件删除
文件拷贝
time
浮点型时间戳
整型时间戳
两个时间戳相减(参数暂定为整型),返回值是一个带 年天时分秒的值

tm_year ：年
tm_mon ：月（1-12）
tm_mday ：日（1-31）
tm_hour ：时（0-23）
tm_min ：分（0-59）
tm_sec ：秒（0-59）
tm_wday ：星期几（0-6,0表示周日）
tm_yday ：一年中的第几天（1-366）
tm_isdst ：是否是夏令时（默认为-1）

'''
import time
from dateutil.parser import parse
class Time: 
    def time_now_f(self):
        '''
        功能:获取时间戳
        参数:无
        返回值:类似这样的1608878746.0280244
        返回值类型:float
        '''
        return time.time()
    def time_now_i(self):
        '''
        功能:获取当前时间的时分秒
        '''
        return int(time.time())
    def time_s(self,data):
        '''
        睡眠几秒
        '''
        time.sleep(data)
    def time_difference(self):
        '''
        时间差
        ##因为要判断闰年,年数暂时没有加##
        '''
        time1='1608878746'
        time2='1699999000'
        time3=int(time2)-int(time1)
        print(time3,"秒")
        #如果秒数大于60转为分钟
        if time3>60:
            time4=time3//60
            #如果分钟大于60转为小时
            print(time4,"分",time3-time4*60,"秒")
            if time4>60:
                time5=time4//60
                print(time5,"小时",time4-time5*60,"分",time3-time4*60,"秒")
                if time5>24:
                    time6=time5//24
                    print(time6,"天",time5-time6*24,"小时",time4-time5*60,"分",time3-time4*60,"秒")

