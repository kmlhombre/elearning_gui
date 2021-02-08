import wx

from errorWindow import errorFrame
from successWindow import successFrame


class addGradeFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="Add Grade")
        self.SetSize(400, 300)
        self.SetBackgroundColour('pink')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        sizer = wx.BoxSizer()
        sizer.AddStretchSpacer(1)
        sizer.Add(panel, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer(1)

        self.SetSizer(sizer)

        self.text_ctrl1 = wx.TextCtrl(panel)
        self.text_ctrl2 = wx.TextCtrl(panel)
        self.text_ctrl3 = wx.TextCtrl(panel)

        my_btn = wx.Button(panel, label='Confirm', pos=(20, 20), size=(300, 50))

        # akcje obiektow
        self.text_ctrl1.AppendText("Student")
        self.text_ctrl2.AppendText("Subject")
        self.text_ctrl3.AppendText("Grade")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        # rozmieszczenie obiektow w oknie
        my_sizer.Add(self.text_ctrl1, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(self.text_ctrl2, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(self.text_ctrl3, 0, wx.ALL | wx.EXPAND, 4)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):

        # TODO
        student_name = self.text_ctrl1.GetValue()
        subject = self.text_ctrl2.GetValue()
        grade =  self.text_ctrl3.GetValue()

        # TODO add grades to the database. Call proper function.
        # TODO get response message?
        isGradeAdded = False
        # close modal on success
        b = event.GetEventObject()
        print(b.GetLabel(), "Add grade success")
        self.Hide()

        if isGradeAdded:
            successFrame()
        else:
            errorFrame('Some error has occured')


