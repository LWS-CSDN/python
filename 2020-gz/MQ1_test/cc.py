import wx
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        icon=wx.EmptyIcon()
        icon.LoadFile("logo.ico",wx.BITMAP_TYPE_ICO)
        frame.SetIcon(icon)
        frame.tbicon=wx.TaskBarIcon()
        frame.tbicon.SetIcon(icon,"wxPython Demo")
        return True
app = App()
app.MainLoop()