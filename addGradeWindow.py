import wx


class addGradeFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title="elearning")
        self.SetSize(300, 300)
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        #TODO
        # pobrac studentow(tych ktorzy sa wlasnie wyswietlani w tablei w okienku teacherFrame) z bazy danych
        students = ["Adam Kowalski", "Jan Nowak", "..."]
        #elementy zawarte w oknie
        self.txt = wx.TextCtrl(panel)
        my_btn = wx.Button(panel, label='Add')
        students_combobox = wx.Choice(self, choices=students)

        #akcje obiektow
        self.txt.AppendText("Grade (From 1 to 6)")
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        students_combobox.SetSelection(0)

        #rozmieszczenie obiektow w oknie

        my_sizer.Add(self.txt, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(students_combobox, 0, wx.ALL | wx.CENTER, 5)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        #TODO
        # wpisac nowa ocene do bazy
        newGrade = self.txt.GetValue()
        self.Hide()
