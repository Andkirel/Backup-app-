import customtkinter
import tkinter

class Create_User(customtkinter.CTk):
    def __init__(self):
        pass
    def UserB(self):

        self.Middle_frame_UB = customtkinter.CTkFrame(self, width=850, height=500, corner_radius=10)
        self.Middle_frame_UB.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)

        self.Create_User_label = customtkinter.CTkLabel(self.Middle_frame_UB, text="Create Account", anchor="w",font=customtkinter.CTkFont(size=30, weight="bold"))
        self.Create_User_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.Username_entry = customtkinter.CTkEntry(self.Middle_frame_UB, width=250, height=25, corner_radius=10,placeholder_text="Username")
        self.Username_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.Pin_entry = customtkinter.CTkEntry(self.Middle_frame_UB, width=250, height=25, corner_radius=10,placeholder_text="4 digit Pin")
        self.Pin_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.CPin_entry = customtkinter.CTkEntry(self.Middle_frame_UB, width=250, height=25, corner_radius=10,placeholder_text="Confirm Pin")
        self.CPin_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.Create_Account_Button = customtkinter.CTkButton(self.Middle_frame_UB, text="Create Account", command=self.PinChecking)
        self.Create_Account_Button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.Answer = customtkinter.CTkLabel(self.Middle_frame_UB, text='')
        self.Answer.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


    def PinChecking(self):
        Pins = self.Pin_entry.get()
        CPins = self.CPin_entry.get()
        if CPins != Pins:
            self.Answer.config(text="The pins do not match")
        elif CPins == Pins:
            self.Answer.config(text="Account has been created!")