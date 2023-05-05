import customtkinter
import main
import tkinter

class Backupbutton(customtkinter.CTk):
    def __call__(self):
        self.Middle_frame = customtkinter.CTkFrame(self, width=850, height=500, corner_radius=10)
        self.Middle_frame.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)