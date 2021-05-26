import wx
import wx.adv
import webbrowser
import os



#pip install https://wxpython.org/Phoenix/snapshot-builds/wxPython-4.1.2a1.dev5075+06d08743-cp37-cp37m-win_amd64.whl
class FolderBookmarkTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = '/logo.ico'
    TITLE = '标题'

    MENU_ID1, MENU_ID2 = wx.NewIdRef(count=2)

    def __init__(self):
        super().__init__()

        # 设置图标和提示
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)
        
       
        # 绑定菜单项事件
        self.Bind(wx.EVT_MENU, self.onOne, id=self.MENU_ID1)
        self.Bind(wx.EVT_MENU, self.onExit, id=self.MENU_ID2)

        # self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        # self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        #self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouse)
        #Bind(wx.EVT_LEFT_DCLICK,self.OnTaskBarLeftDClick)
        # self.Bind(wx.)
        
    def OnTaskBarLeftDClick(self):
        print("123")
        self.PopupMenu(self.CreatePopupMenu()) 

    def CreatePopupMenu(self):
        '''生成菜单'''
        print("菜单")
        menu = wx.Menu()
        # 添加两个菜单项
        menu.Append(self.MENU_ID1, '弹个框')
        menu.Append(self.MENU_ID2, '退出')
        return menu

    def onOne(self, event):
        print("111")

        webbrowser.open('http://www.baidu.com')
        #wx.MessageBox('111')

    def onExit(self, event):
        print('222')
        wx.Exit()

    def OnLeftDown(self, evt):
        '''左键按下事件函数'''
        print("123")
       
        #self.tip.SetLabel(u'左键按下')
    def OnLeftUp(self, evt):
        '''左键弹起事件函数'''
        print("123")
        
        #self.tip.SetLabel(u'左键弹起')
    
    def OnMouse(self, evt):
        '''鼠标事件函数'''
        print("123")
        #self.tip.SetLabel(str(evt.EventType))
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__()
        FolderBookmarkTaskBarIcon()
        #wx.EVT_TASKBAR_LEFT_UP(self.tbicon, self.OnTaskBarLeftClick)
        #self.tbicon.Bind(wx.adv.EVT_TASKBAR_LEFT_UP,self.OnTaskBarLeftClick)
        #wx.EVT_TREE_STATE_IMAGE_CLICK(self.tbicon, self.OnTaskBarLeftClick)
    # def OnTaskBarLeftClick(self):   
    #     print("123")
    #     self.PopupMenu(self.tbicon.CreatePopupMenu()) 

class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True


if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()