import customtkinter
import tkinter

class Backupbutton(customtkinter.CTk):
    def __init__(self):
        pass
    def BackupB(self):
        str1 = tkinter.StringVar()

        self.Middle_frame = customtkinter.CTkFrame(self, width=850, height=500, corner_radius=10)
        self.Middle_frame.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)

        self.File_entry1 = customtkinter.CTkEntry(self.Middle_frame, width=450,height=25,corner_radius=10, placeholder_text="File Path", textvariable=str1)
        self.File_entry1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.Multi_Files = customtkinter.CTkCheckBox(self.Middle_frame,width=25,height=25, text="Add another File")
        self.Multi_Files.place(relx=0.85, rely=0.2, anchor=tkinter.CENTER)

    #def Check_Box_event(self):
        #str2 = tkinter.StringVar()
        #self.File_entry2 = customtkinter.CTkEntry(self.Middle_frame, width=450, height=25, corner_radius=10,placeholder_text="File Path", textvariable=str2)
        #self.File_entry2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)