import wx

from changePasswordWindow import changePasswordFrame
from wx.lib.agw import ultimatelistctrl as ULC

class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        boldfont = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        boldfont.SetWeight(wx.BOLD)
        boldfont.SetPointSize(12)

        self.ulc = ULC.UltimateListCtrl(self, agwStyle = wx.LC_REPORT
                                         | wx.LC_VRULES
                                         | wx.LC_HRULES
                                         | ULC.ULC_HAS_VARIABLE_ROW_HEIGHT)

        info = ULC.UltimateListItem()
        info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_CHECK
        info._image = []
        info._format = 0
        info._kind = 1
        info._text = "Student"
        self.ulc.InsertColumnInfo(0, info)

        info = ULC.UltimateListItem()
        info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT | ULC.ULC_MASK_CHECK
        info._image = []
        info._format = 0
        info._kind = 1
        info._text = "Add Grade"
        self.ulc.InsertColumnInfo(1, info)

        for index in range(2, 20):
            info = ULC.UltimateListItem()
            info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
            info._format = 0
            info._text = "Grade"
            info._image = []
            self.ulc.InsertColumnInfo(index, info)

        self.button1 = wx.Button(self.ulc, -1, "+")
        for index in range(20):
            self.ulc.SetItemWindow(index, 0, self.button1)

        self.Bind(wx.EVT_BUTTON, self.OnButton)

        self.ulc.InsertStringItem(0, "Newsboys")
        self.ulc.SetStringItem(0, 1, "Go")
        self.ulc.SetStringItem(0, 2, "Rock")

        self.ulc.InsertStringItem(1, "Puffy")
        self.ulc.SetStringItem(1, 1, "Bring It!")
        self.ulc.SetStringItem(1, 2, "Pop")

        self.ulc.InsertStringItem(2, "Family Force 5")
        self.ulc.SetStringItem(2, 1, "III")
        self.ulc.SetStringItem(2, 2, "Crunk")

        self.ulc.SetColumnWidth(0, 150)
        self.ulc.SetColumnWidth(1, 200)
        self.ulc.SetColumnWidth(2, 100)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.ulc, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def OnButton(self,event):
        b= event.GetEventObject()
        print(b.GetLabel(),"pressed")


class teacherPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}
        self.current_folder_path = None

        #stworzenie tabeli
        self.list_ctrl = ULC.UltimateListCtrl(self, agwStyle = wx.LC_REPORT
                                         | wx.LC_VRULES
                                         | wx.LC_HRULES
                                         | ULC.ULC_HAS_VARIABLE_ROW_HEIGHT)
        info = ULC.UltimateListItem()
        info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info._format = 0
        info._text = "Subject"
        info._image = []
        self.list_ctrl.InsertColumnInfo(0, info)

        for index in range(1, 20):
            info = ULC.UltimateListItem()
            info._mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
            info._format = 0
            info._text = "Grade"
            info._image = []
            self.list_ctrl.InsertColumnInfo(index, info)

        self.list_ctrl.InsertStringItem(0, "Newsboys")
        self.list_ctrl.SetStringItem(0, 1, "Go")
        self.list_ctrl.SetStringItem(0, 2, "Rock")

        self.list_ctrl.InsertStringItem(1, "Puffy")
        self.list_ctrl.SetStringItem(1, 1, "Bring It!")
        self.list_ctrl.SetStringItem(1, 2, "Pop")

        self.list_ctrl.InsertStringItem(2, "Family Force 5")
        self.list_ctrl.SetStringItem(2, 1, "III")
        self.list_ctrl.SetStringItem(2, 2, "Crunk")
        #TODO
        #pobranie danych o przedmiotach i ocenach

        '''
        dodawanie danych do tabeli:
        self.list_ctrl.InsertItem(index_of_row, "Math")
        self.list_ctrl.SetItem(index_of_row, index_of_column, "2")
        '''

        #dodawanie obiektow

        logout_button = wx.Button(self, label="Logout")
        change_password_button = wx.Button(self, label="Change Password")

        #akcje obiektorw
        logout_button.Bind(wx.EVT_BUTTON, self.on_press_logout)
        change_password_button.Bind(wx.EVT_BUTTON, self.on_press_chngpass)

        #rozmieszczenie obiektow
        main_sizer.Add(self.list_ctrl, 1, wx.EXPAND)
        main_sizer.Add(logout_button, 0, wx.ALL | wx.CENTER, 5)
        main_sizer.Add(change_password_button, 0, wx.ALL | wx.CENTER, 5)

        self.SetSizer(main_sizer)

    def on_press_chngpass(self, event):
        changePasswordFrame()

    def on_press_logout(self, event):
        exit()


class teacherFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="elearning")
        self.SetSize(1280, 720)
        self.panel = TestPanel(self)
        self.Show()