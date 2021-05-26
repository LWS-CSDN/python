import celery
import time
from celery import Celery, platforms

platforms.C_FORCE_ROOT = True  #加上这一行

backend='redis://127.0.0.1:6379/db0'
broker='redis://127.0.0.1:6379/db1'

cel=celery.Celery('test',backend=backend,broker=broker)
@cel.task
def send_email(name):
    print("向%s发送邮件..."%name)
    time.sleep(5)
    print("向%s发送邮件完成"%name)
    return "ok"