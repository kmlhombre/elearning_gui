import wx

class parentFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="elearning")
        self.SetSize(300, 300)
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl1 = wx.TextCtrl(panel)
        text_ctrl2 = wx.TextCtrl(panel)
        self.text_ctrl1.AppendText("Login")
        text_ctrl2.AppendText("Password")
        my_sizer.Add(self.text_ctrl1, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(text_ctrl2, 0, wx.ALL | wx.EXPAND, 4)
        my_btn = wx.Button(panel, label='Log in')
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl1.GetValue()
        #frame = parentWindow()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You typed: "{value}"')