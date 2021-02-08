import wx

from addGradeWindow import addGradeFrame
from changePasswordWindow import changePasswordFrame


class teacherPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}
        self.current_folder_path = None

        #stworzenie tabeli
        self.list_ctrl = wx.ListCtrl(self, size=(-1, 300), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, "Subject", width=140)
        for index in range(1, 20):
            self.list_ctrl.InsertColumn(index, "Grade", width=60)

        #TODO
        #pobranie danych o przedmiotach i ocenach

        '''
        dodawanie danych do tabeli:
        self.list_ctrl.InsertItem(index_of_row, "Math")
        self.list_ctrl.SetItem(index_of_row, index_of_column, "2")
        '''
        #TODO
        # subjetcs to tablica gdzie beda pobrane z bazy przedmioty zalogowanego nauczyciela

        subjects = ["Math", "Phisics", "IT"]

        #dodawanie obiektow
        subjects_combobox = wx.Choice(self, choices=subjects)
        add_grade_button = wx.Button(self, label="Add grade")
        logout_button = wx.Button(self, label="Logout")
        change_password_button = wx.Button(self, label="Change Password")

        #akcje obiektorw
        subjects_combobox.SetSelection(0)
        subjects_combobox.Bind(wx.EVT_CHOICE, self.on_combo)
        logout_button.Bind(wx.EVT_BUTTON, self.on_press_logout)
        change_password_button.Bind(wx.EVT_BUTTON, self.on_press_chngpass)
        add_grade_button.Bind(wx.EVT_BUTTON, self.on_press_add_grade)

        #rozmieszczenie obiektow
        main_sizer.Add(self.list_ctrl, 1, wx.EXPAND)
        main_sizer.Add(subjects_combobox, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(add_grade_button, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(logout_button, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(change_password_button, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)
    #TODO
    # pobiera i wyswietla nowa klase z przedmitoem
    def on_combo(self, event):
        print("ELO")

    def on_press_add_grade(self, event):
        addGradeFrame()

    def on_press_chngpass(self, event):
        changePasswordFrame()

    def on_press_logout(self, event):
        exit()


class teacherFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="elearning")
        self.SetSize(1280, 720)
        self.panel = teacherPanel(self)
        self.Show()