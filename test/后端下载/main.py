#!/usr/bin/python
#encoding:utf-8
import urllib
import os
def Schedule(a,b,c):
'''''
       a:已经下载的数据块
       b:数据块的大小
       c:远程文件的大小
'''
per = 100.0 * a * b / c
if per > 100 :
per = 100
print '%.2f%%' % per
url = 'http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
local = os.path.join( '/data/software' , 'Python-2.7.5.tar.bz2' )
urllib.urlretrieve(url,local,Schedule)

