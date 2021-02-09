'''
python进程池,线程池与异步调用,回调机制
'''

'''
#1.进程池、线程池使用案例
'''
# from concurrent.futures import ProcessPoolExecutor  # 进程池模块
# from concurrent.futures import ThreadPoolExecutor  # 线程池模块
# import os, time, random

# #  下面是以进程池为例， 线程池只是模块改一下即可
# def talk(name):
#     print('name: %s  pis%s  run' % (name,os.getpid()))
#     time.sleep(random.randint(1, 3.虚拟DOM的两种创建方式))

# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(4)  # 设置线程池大小，默认等于cpu核数
#     for i in range(10):
#         pool.submit(talk, '进程%s' % i)  # 异步提交（只是提交需要运行的线程不等待）

#     # 作用1：关闭进程池入口不能再提交了   作用2：相当于jion 等待进程池全部运行完毕
#     pool.shutdown(wait=True)  
#     print('主进程')


'''
#2.异步回调与同步调用
'''
# concurrent.futures模块提供了高度封装的异步调用接口
# ThreadPoolExecutor：线程池，提供异步调用
# ProcessPoolExecutor: 进程池，提供异步调用

#2.0同步调用
# from concurrent.futures import ProcessPoolExecutor  # 进程池模块
# import os, time, random


# # 1、同步调用： 提交完任务后、就原地等待任务执行完毕，拿到结果，再执行下一行代码（导致程序串行执行）
# def talk(name):
#     print('name: %s  pis%s  run' % (name,os.getpid()))
#     time.sleep(random.randint(1, 3.虚拟DOM的两种创建方式))

# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(4)
#     for i in range(10):
#         pool.submit(talk, '进程%s' % i).result()  # 同步迪奥用，result()，相当于join 串行

#     pool.shutdown(wait=True)
#     print('主进程')

#2.1异步调用
# from concurrent.futures import ProcessPoolExecutor  # 进程池模块
# import os, time, random

# def talk(name):
#     print('name: %s  pis%s  run' % (name,os.getpid()))
#     time.sleep(random.randint(1, 3.虚拟DOM的两种创建方式))
#     print(name+'已完成')

# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(4)
#     for i in range(10):
#         pool.submit(talk, '进程%s' % i)  # 异步调用，不需要等待

#     pool.shutdown(wait=True)
#     print('主进程')


#2.2回调机制
# import time
# import requests
# from concurrent.futures import ThreadPoolExecutor  # 线程池模块

# def get(url):
#     print('GET %s' % url)
#     response = requests.get(url)  # 下载页面
#     time.sleep(3.虚拟DOM的两种创建方式)  # 模拟网络延时
#     return {'url': url, 'content': response.text}  # 页面地址和页面内容

# def parse(res):
#     res = res.result()  # !取到res结果 【回调函数】带参数需要这样
#     print('%s res is %s' % (res['url'], len(res['content'])))

# if __name__ == '__main__':
#     urls = {
#         'http://www.baidu.com',
#         'http://www.360.com',
#         'http://www.iqiyi.com'
#     }
#     pool = ThreadPoolExecutor(2)
#     for i in urls:
#         pool.submit(get, i).add_done_callback(parse)  # 【回调函数】执行完线程后，跟一个函数 

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests

# 给线程池设置最大工作的线程数
pool = ThreadPoolExecutor(10)
urls = [
    
]


def task(url):
    response = requests.get(url)
    return response


# response会传递到call_back的参数中
def call_back(response):
    # 拿到的是一个future的对象
    # 从对象中取出task中返回的结果
    response.result()
    # 对回调过来的信息进行解析
    pass


for url in urls:
    # 使用回调函数能够用返回的结果实时的去解析, 实现异步非阻塞
    pool.submit(task, url).add_done_callback(call_back)

# 如果使用shutdown会等待所有任务执行结束后再去执行主线程中的代码
# pool.shutdown(True)