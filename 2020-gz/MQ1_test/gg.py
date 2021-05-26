import wx

TIMER_ID = 100

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(350,200))
        self.timer = None
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

    def OnDoubleClick(self, event):
        self.timer.Stop()
        print("double click")

    def OnSingleClick(self, event):
        print("single click")
        self.timer.Stop()

    def OnLeftDown(self, event):
        self.timer = wx.Timer(self, TIMER_ID)
        self.timer.Start(200) # 0.2 seconds delay
        wx.EVT_TIMER(self, TIMER_ID, self.OnSingleClick)



app = wx.App(redirect=True)
top = Frame("Hello World")
top.Show()
app.MainLoop()