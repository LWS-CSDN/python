
# def wx_py(data,data1,URL,Code=True):
#     ICON=data
#     TITLE=data1
#     import os
#     if os.name=='nt':
#         import webbrowser
#         #import subprocess
#         import time
        # def excuteCommand(com):
        #     ex = subprocess.Popen(com, stdout=subprocess.PIPE, shell=True)
        #     out, err  = ex.communicate()
        #     status = ex.wait()
        #     #print("cmd in:", com)
        #     #print("cmd out: ", out.decode('gb2312'))   

        # com='pip install https://wxpython.org/Phoenix/snapshot-builds/wxPython-4.1.2a1.dev5075+06d08743-cp37-cp37m-win_amd64.whl'
        # excuteCommand(com)
        #time.sleep(1)
           

        

        
        # t2=threading.Thread(target=app1.ShowBalloon,args=('123','456',))
        # t2.start()

#wx_py()
# import threading
# t1=threading.Thread(target=wx_py,args=('G:/CSDN_L/python/MQ1_test/logo.ico','麻雀','http://www.baidu.com',))
# t1.start()



import wx 
import wx.adv
ICON='G:/CSDN_L/python/MQ1_test/logo.ico'
TITLE='麻雀'
URL='http://www.baidu.com'
class BibTaskBarIcon(wx.adv.TaskBarIcon): 
    MENU_ID1, MENU_ID2 = wx.NewIdRef(count=2)
    def __init__(self, frame): 
        wx.adv.TaskBarIcon.__init__(self) 
        self.frame = frame 
        icon = wx.Icon(ICON, wx.BITMAP_TYPE_ICO) 
        self.SetIcon(icon, TITLE) 
        #self.Bind(wx.EVT_MENU, self.onOne, id=self.MENU_ID1)
        self.Bind(wx.EVT_MENU, self.onExit, id=self.MENU_ID2)
        # if Code:
        #     self.ShowBalloon('123','456',msec=0,flags=0)
        #time.sleep(3.虚拟DOM的两种创建方式)
        #self.ShowBalloon('456','789',msec=0,flags=0)

    def CreatePopupMenu_1(self): 
        print('左击')
        # webbrowser.open(URL) 
        # self.menu = wx.Menu() 
        # self.menu.Append(self.MENU_ID1, "") 
        # self.menu.Append(self.MENU_ID2, "") 
        # return self.menu 
    # def ShowBalloon(self, title, text, msec, flags):
    #     print("气泡")
    #     return super().ShowBalloon(title, text, msec=msec, flags=flags)     
    def CreatePopupMenu(self):
        '''生成菜单'''
        #print("菜单")
        menu = wx.Menu()
        # 添加两个菜单项
        #menu.Append(self.MENU_ID1, '弹个框')
        menu.Append(self.MENU_ID2, '退出')
        return menu
    def onOne(self, event):
        wx.MessageBox('111')
    def onExit(self, event):
        wx.Exit()
class TaskBarFrame(wx.Frame): 
    def __init__(self, parent, title): 
        wx.Frame.__init__(self, parent, style=wx.FRAME_NO_TASKBAR) 
        self.tbicon = BibTaskBarIcon(self) 
        self.tbicon.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK,self.OnTaskBarLeftClick)      
    def OnTaskBarLeftClick(self, e): 
        self.tbicon.CreatePopupMenu_1()
    def show(self,title, text, msec, flags):  
        self.tbicon.ShowBalloon(title, text, msec, flags)
        # t2=threading.Thread(target=bb,args=('123','456',0,0,))
        # t2.start()

import time
def wx_py():
    app = wx.App(False) 
    cc=TaskBarFrame(None,"testing frame") 
    cc.show('123','456',0,0)
    cc.show('456','789',0,0)
    app.MainLoop()
    
    
    # t1=threading.Thread(target=app.MainLoop)
    # t1.start()
    #cc.show('123','456',0,0)
    
   


    

import threading
t1=threading.Thread(target=wx_py)
t1.start()


# bbb=BibTaskBarIcon()
# bbb.ShowBalloon('123','456',msec=0,flags=0)



# def wx_py_pop(data,data1):
#     ICON=data
#     TITLE=data1
#     import wx 
#     import wx.adv
#     class BibTaskBarIcon(wx.adv.TaskBarIcon): 
#         def __init__(self, frame): 
#             wx.adv.TaskBarIcon.__init__(self) 
#             self.frame = frame 
#             icon = wx.Icon(ICON, wx.BITMAP_TYPE_ICO) 
#             self.SetIcon(icon, TITLE) 
#         def ShowBalloon(self, title, text, msec, flags):
#             return super().ShowBalloon(title, text, msec=msec, flags=flags) 

# import threading
# t1=threading.Thread(target=wx_py,args=('','麻雀','http://www.baidu.com',))
# t1.start()
# t2=threading.Thread(target=wx_py_pop,args=(''))
# t2.start()










    



