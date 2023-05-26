import customtkinter
import tkinter
import re
import PostGres


class Create_User:

    def UserB(self,app):
        self.app = app

        app.Middle_frame_UB = customtkinter.CTkFrame(app, width=850, height=500, corner_radius=10)
        app.Middle_frame_UB.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)

        app.Create_User_label = customtkinter.CTkLabel(app.Middle_frame_UB, text="Create Account", anchor="w",font=customtkinter.CTkFont(size=30, weight="bold"))
        app.Create_User_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        app.Username_entry = customtkinter.CTkEntry(app.Middle_frame_UB, width=250, height=25, corner_radius=10,placeholder_text="Username")
        app.Username_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        app.Pin_entry = customtkinter.CTkEntry(app.Middle_frame_UB, width=250, height=25, corner_radius=10,placeholder_text="4 digit Pin")
        app.Pin_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        app.CPin_entry = customtkinter.CTkEntry(app.Middle_frame_UB, width=250, height=25, corner_radius=10,placeholder_text="Confirm Pin")
        app.CPin_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        app.Create_Account_Button = customtkinter.CTkButton(app.Middle_frame_UB, text="Create Account", command=self.PinChecking)
        app.Create_Account_Button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        app.Answer = customtkinter.CTkLabel(app.Middle_frame_UB, text='')
        app.Answer.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


    def PinChecking(self):
        number_checker = re.compile(r'\d\d\d\d')

        Pins = self.app.Pin_entry.get()
        self.Pins = Pins
        UserID = self.app.Username_entry
        self.UserID = UserID

        CPins = self.app.CPin_entry.get()
        if CPins != Pins or not number_checker.match(Pins) or not number_checker.match(CPins):
            self.app.Answer.configure(text="The pins do not match or is not 4 digits")
        elif CPins == Pins:
            self.app.Answer.configure(text="Account has been created!")
