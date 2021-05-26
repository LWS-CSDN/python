#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
author:L
time:2020-12-25
python3.9.1
"""
import shutil
class L_shuil:
    def copyfileobj(self):
        '''
        拷贝内容
        记得关闭文件夹
        第一个文件夹的内容存在,第二个如果存在同名则覆盖,第二个文件夹下如果没有这个文件则自动创建
        '''
        shutil.copyfileobj(open('456/1.txt','r'), open('123/2.txt', 'w')) 
    def copyfile(self,src,dst):
        '''
        拷贝文件
        '''
        shutil.copyfile(src,dst) 
    def copytree(self,src,dst):
        '''
        递归的去拷贝文件夹
        '''
        shutil.copytree(src,dst)
    def remove(self,dir):
        '''
        递归的去删除文件
        '''
        shutil.rmtree(dir)
    def move(self,src,dst):
        '''
        递归的去移动文件，它类似mv命令，其实就是重命名。
        '''
        shutil.move(src,dst)
