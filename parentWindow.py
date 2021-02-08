import wx
from changePasswordWindow import changePasswordFrame

class parentPanel(wx.Panel):
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

        logout_button = wx.Button(self, label="Logout")
        change_password_button = wx.Button(self, label="Change Password")
        logout_button.Bind(wx.EVT_BUTTON, self.on_press_logout)
        change_password_button.Bind(wx.EVT_BUTTON, self.on_press_chngpass)

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(logout_button, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(change_password_button, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    def on_press_chngpass(self, event):
        changePasswordFrame()

    def on_press_logout(self, event):
        exit()


class parentFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="elearning Parent")
        self.SetSize(1280, 720)
        self.panel = parentPanel(self)
        self.Show()
