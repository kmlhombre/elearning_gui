import wx

from addGradeWindow import addGradeFrame
from changePasswordWindow import changePasswordFrame


class teacherPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.GridBagSizer(10, 10)
        self.row_obj_dict = {}
        self.current_folder_path = None

        # stworzenie tabeli
        self.list_ctrl = wx.ListCtrl(self, size=(-1, 600), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        # stworzenie tabeli

        self.list_ctrl.InsertColumn(0, "Subject", width=140)
        self.list_ctrl.InsertColumn(1, "Student", width=60)
        self.list_ctrl.InsertColumn(2, "Grade", width=60)

        self.list_ctrl.InsertStringItem(0, "Newsboys")
        self.list_ctrl.SetStringItem(0, 1, "Go")
        self.list_ctrl.SetStringItem(0, 2, "Rock")

        self.list_ctrl.InsertStringItem(1, "Puffy")
        self.list_ctrl.SetStringItem(1, 1, "Bring It!")
        self.list_ctrl.SetStringItem(1, 2, "Pop")

        self.list_ctrl.InsertStringItem(2, "Family Force 5")
        self.list_ctrl.SetStringItem(2, 1, "III")
        self.list_ctrl.SetStringItem(2, 2, "Crunk")

        self.list_ctrl.SetColumnWidth(0, 150)
        self.list_ctrl.SetColumnWidth(1, 200)
        self.list_ctrl.SetColumnWidth(2, 100)

        # dodawanie obiektow

        logout_button = wx.Button(self, label="Logout", size=(100, 50))
        logout_button.SetBackgroundColour('orange')
        change_password_button = wx.Button(self, label="Change Password", size=(100, 50))
        change_password_button.SetBackgroundColour('pink')
        add_grade_button = wx.Button(self, label="Add Grade", size=(100, 50))
        add_grade_button.SetBackgroundColour(wx.Colour(137, 207, 240))
        # akcje obiektorw
        add_grade_button.Bind(wx.EVT_BUTTON, self.on_add_grade)

        logout_button.Bind(wx.EVT_BUTTON, self.on_press_logout)
        change_password_button.Bind(wx.EVT_BUTTON, self.on_press_chngpass)

        # rozmieszczenie obiektow
        main_sizer.Add(self.list_ctrl, pos=(0, 0), flag = wx.EXPAND|wx.ALL)
        main_sizer.Add(change_password_button, pos=(0, 2))
        main_sizer.Add(add_grade_button, pos=(0, 1))
        main_sizer.Add(logout_button, pos=(0, 3))

        self.SetSizer(main_sizer)

    def on_press_chngpass(self, event):
        changePasswordFrame()

    def on_press_logout(self, event):
        exit()

    def on_add_grade(self, event):
        # todo launch new modal withing you can input grades
        b = event.GetEventObject()
        # TODO get item object: student, grade and subject and add new row
        print(b.GetLabel(), "Add grade")
        # TODO pass object (row) as param to  **addGradeFrame(param)**
        addGradeFrame()


class teacherFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="elearning Teacher")
        self.SetSize(810,600)
        self.panel = teacherPanel(self)
        self.Show()
