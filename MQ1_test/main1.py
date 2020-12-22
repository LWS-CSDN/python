
import wx
import wx.adv
 
 
class Balloon(wx.adv.TaskBarIcon):
    ICON = "logo.ico"
    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON))
 
    # Menu数据
    def setMenuItemData(self):
        return (("Config", self.OnConfig), ("About", self.OnAbout), ("Close", self.OnClose))
    
    # 创建菜单
    def CreatePopupMenu(self):
        menu = wx.Menu()
        for itemName, itemHandler in self.setMenuItemData():
            if not itemName:    # itemName为空就添加分隔符
                menu.AppendSeparator()
                continue
            menuItem = wx.MenuItem(None, wx.ID_ANY, text=itemName, kind=wx.ITEM_NORMAL) # 创建菜单项
            menu.AppendItem(menuItem)                                                   # 将菜单项添加到菜单
            self.Bind(wx.EVT_MENU, itemHandler, menuItem)
        return menu
 
    def OnConfig(self, event):
        pass
 
    def OnAbout(self, event):
        pass
 
    def OnClose(self, event):
        pass
 
 
class myFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)
        self.taskBarIcon = Balloon()
 
if __name__ == '__main__':
    app = wx.App()
    frame = myFrame()
    frame.Show()
    app.MainLoop()