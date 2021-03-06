import wx

from addGradeWindow import addGradeFrame
from changePasswordWindow import changePasswordFrame

class teacherPanel(wx.Panel):

    def __init__(self, parent, logged_user):
        super().__init__(parent)
        main_sizer = wx.GridBagSizer(10, 10)
        self.row_obj_dict = {}
        self.current_folder_path = None

        self.logged_user_id = logged_user

        # stworzenie tabeli
        self.list_ctrl = wx.ListCtrl(self, size=(700, 600), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, "Subject", width=140)
        self.list_ctrl.SetColumnWidth(0, 120)
        self.list_ctrl.SetScrollbar(wx.HORIZONTAL, 0, 16, 50)
        for index in range(1, 20):
            self.list_ctrl.InsertColumn(index, "Grade", width=60)
            self.list_ctrl.SetColumnWidth(index, 60)

        #TODO tutaj funkcja ktora pobiera dane tj.
        #przedmioty
        #uczniow i oceny pierwszego przedmiotu

        self.subjects = ["Math", "IT", "..."]
        self.students = ["Adam Kowalski"]

        # dodawanie obiektow
        logout_button = wx.Button(self, label="Logout", size=(100, 50))
        logout_button.SetBackgroundColour('orange')
        self.subject_choice = wx.Choice(self, choices=self.subjects, size=(100,100))
        change_password_button = wx.Button(self, label="Change Password", size=(100, 50))
        change_password_button.SetBackgroundColour('pink')
        add_grade_button = wx.Button(self, label="Add Grade", size=(100, 50))
        add_grade_button.SetBackgroundColour(wx.Colour(137, 207, 240))

        # akcje obiektorw
        self.subject_choice.SetSelection(0)
        self.subject_choice.Bind(wx.EVT_CHOICE, self.on_choice)
        add_grade_button.Bind(wx.EVT_BUTTON, self.on_add_grade)
        logout_button.Bind(wx.EVT_BUTTON, self.on_press_logout)
        change_password_button.Bind(wx.EVT_BUTTON, self.on_press_chngpass)

        #uzupelnianie tabeli danymi z pierwszego przedmiotu
        self.fill_table(subject=self.subject_choice.GetLabel())

        # rozmieszczenie obiektow
        main_sizer.Add(self.list_ctrl, pos=(1, 1), flag = wx.EXPAND|wx.ALL)
        main_sizer.Add(change_password_button, pos=(1, 4))
        main_sizer.Add(add_grade_button, pos=(1, 3))
        main_sizer.Add(self.subject_choice, pos=(1, 2))
        main_sizer.Add(logout_button, pos=(1, 5))

        self.SetSizer(main_sizer)

    def on_choice(self, event):
        print(self.subjects[self.subject_choice.GetCurrentSelection()]) #wyswietla wybrany przedmiot
        self.fill_table(subject=self.subjects[self.subject_choice.GetCurrentSelection()]) #wypelnia na nowo tabele nowo pobranymi danymi

    def on_press_chngpass(self, event):
        changePasswordFrame(self.logged_user_id)

    def on_press_logout(self, event):
        exit()

    def on_add_grade(self, event):
        addGradeFrame(students=self.students)
        self.fill_table(self.subjects[self.subject_choice.GetCurrentSelection()]) #odswiezenie tablicy

    def fill_table(self, subject):
        # TODO tutaj pobiera uczniow i oceny z wybranego przedmiotu i odswieza tabele
        #czyszczenie tablicy
        self.list_ctrl.DeleteAllItems()
        #wypelnianie tablicy
        self.list_ctrl.InsertItem(0, "Adam Kowalski") # gdzie 0 to indeks wiersza
        for index in range(1, 6):
            self.list_ctrl.SetItem(0, index, str(index)) # gdzie index to indeks kolumny a str(index) to wartość(ocena)

class teacherFrame(wx.Frame):
    def __init__(self, logged_user):
        super().__init__(parent=None, title="elearning Teacher")
        self.SetSize(1280, 720)
        self.panel = teacherPanel(self, logged_user=logged_user)
        self.Show()
