
from concurrent.futures import ThreadPoolExecutor
import threading
import time
 
# 定义一个准备作为线程任务的函数
def action(max):
    print("发起请求:",max)
    time.sleep(max)
    print("%d获取结果:%d"%(max))
    return max+1
# 创建一个包含4条线程的线程池
with ThreadPoolExecutor(max_workers=4) as pool:
    # 使用线程执行map计算
    # 后面元组有3个元素，因此程序启动3条线程来执行action函数
    results = pool.map(action, (5, 10,15,20,25,30))
    # for r in results:
    #     print(r)