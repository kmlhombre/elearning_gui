import wx

from errorWindow import errorFrame
from parentWindow import parentFrame
from studentWindow import studentFrame
from teacherWindow import teacherFrame


class loggingFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="elearning")
        self.SetSize(300, 300)
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        # elementy zawarte w oknie
        self.text_ctrl1 = wx.TextCtrl(panel)
        self.text_ctrl2 = wx.TextCtrl(panel)
        my_btn = wx.Button(panel, label='Log in')

        # akcje obiektow
        self.text_ctrl1.AppendText("Login")
        self.text_ctrl2.AppendText("Password")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        # rozmieszczenie obiektow w oknie
        my_sizer.Add(self.text_ctrl1, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(self.text_ctrl2, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        
        #TODO
        login = self.text_ctrl1.GetValue()
        password = self.text_ctrl2.GetValue()

        #tutaj potrzebna funkcja logujaca

        #na potrzebny testowania
        logged_status = "Student"
        is_logged = True

        if logged_status == "Student" and is_logged:
            studentFrame()
            self.Hide()
        elif logged_status == "Parent" and is_logged:
            parentFrame()
            self.Hide()
        elif logged_status == "Teacher" and is_logged:
            teacherFrame()
            self.Hide()
        else:
            errorFrame()