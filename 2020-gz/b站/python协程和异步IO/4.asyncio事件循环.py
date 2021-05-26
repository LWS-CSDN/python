'''
3.虚拟DOM的两种创建方式.异步编程
'''


'''
3.虚拟DOM的两种创建方式.1事件循环(理解成为一个死循环,去检测并执行某些代码)
伪代码
任务列表=[任务1,任务2,任务3,...]
while True:
    #可执行的任务列表,已完成的任务列表=去任务列表中检测所有的任务,将'可执行'和'已完成'的任务返回
    for 就绪任务 in 可执行的任务列表:
        执行已就绪的任务
    for 已完成的任务 in 一万陈过的任务列表:
        在任务列表中移除 已完成的任务
    如果任务列表中的任务都已完成,则终止循环
'''

import asyncio

#去生成或获取一个事件循环
loop=asyncio.get_event_loop()
#将任务放到'任务列表'
#loop.run_until_complete(任务)
loop.run_until_complete(asyncio.wait(tasks))
