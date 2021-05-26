#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 文件名：thread_download-master.py

import sys
import time
import datetime

from ThreadDownload import *


def show_process(dl):
    while dl.get_complete_rate() < 1:
        complete_rate = int(dl.get_complete_rate()*100)  
        print('\r' + '下载中···（已下载' + str(complete_rate) + '%）', end='', flush=True)
        time.sleep(0.01)


def main():
    try:   
        # Link = input('[+]' + 'Link: ')
        # file_path = input('[+]' + 'File Path: ')
        # thread_number = input('[+]' + 'Thread Number: ')
        # thread_number = int(thread_number)
        #开一个线程用时
        #开两个线程用时
        #开10个线程用时 1921s
        #开100个线程用时
        # start = datetime.now()
        Link='https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe' 
        file_path='./7.exe'
        thread_number=100
        dl = Download(Link, file_path, thread_number)
        dl.download()  
        kaishishijian = time.time()
        print('\n开始下载!')
        show_process(dl)
        print('\r' + '下载中···（已下载' + '100%)', end='', flush=True)
        jieshushijian = time.time()
        print("运行了多久",(datetime.datetime.fromtimestamp(jieshushijian) - datetime.datetime.fromtimestamp(kaishishijian)).seconds,'秒')
        print('\n下载完成!')
        #print("异步用时为：{}".format(datetime.now() - start))

    except Exception:
        print('Parameter Setting Error')
        sys.exit(1)

if __name__=='__main__':
    main()



'''
前端上传文件问题
断点续传,取消上传,

后端下载问题
'''