import wx


class changePasswordFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="elearning")
        self.SetSize(300, 300)
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        #elementy zawarte w oknie
        self.txt = wx.TextCtrl(panel)
        my_btn = wx.Button(panel, label='Change Password')

        #akcje obiektow
        self.txt.AppendText("New Password")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        #rozmieszczenie obiektow w oknie
        my_sizer.Add(self.txt, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        #TODO
        #wpisac nowe haslo do bazy:
        newPassword = self.txt.GetValue()
        self.Hide()