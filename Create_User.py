import customtkinter
import tkinter

class Create_User(customtkinter.CTk):
    def __init__(self):
        pass
    def UserB(self):
        UserID = chr()
        Pin = int
        CPin = int
        EntryID = UserID

        self.Middle_frame = customtkinter.CTkFrame(self, width=850, height=500, corner_radius=10)
        self.Middle_frame.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)

        self.Create_User_label = customtkinter.CTkLabel(self.Middle_frame, text="Create Account", anchor="w",font=customtkinter.CTkFont(size=30, weight="bold"))
        self.Create_User_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.Username_entry = customtkinter.CTkEntry(self.Middle_frame, width=250, height=25, corner_radius=10,placeholder_text="Username", textvariable=UserID, command= UserID_Event)
        self.Username_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.Pin_entry = customtkinter.CTkEntry(self.Middle_frame, width=250, height=25, corner_radius=10,placeholder_text="4 digit Pin", textvariable=Pin)
        self.Pin_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.CPin_entry = customtkinter.CTkEntry(self.Middle_frame, width=250, height=25, corner_radius=10,placeholder_text="Confirm Pin", textvariable=CPin)
        self.CPin_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.Create_Account_Button = customtkinter.CTkButton(self.Middle_frame, text="Create Account",command=self.Backup_button_event1)
        self.Create_Account_Button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def UserID_Event(self):
        if()