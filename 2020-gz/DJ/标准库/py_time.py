#!/usr/bin/python
#coding=utf-8
'''


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

