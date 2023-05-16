import customtkinter
import tkinter

class Backupbutton(customtkinter.CTk):
    def __init__(self):
        pass
    def BackupB(self):



        self.Middle_frame = customtkinter.CTkFrame(self, width=850, height=500, corner_radius=10)
        self.Middle_frame.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)
        self.Sub_frame = customtkinter.CTkFrame(self.Middle_frame, width=550, height=200, corner_radius=10)
        self.Sub_frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.File_entry1 = customtkinter.CTkEntry(self.Middle_frame, width=450,height=25,corner_radius=10, placeholder_text="File Path")
        self.File_entry1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.Multi_Files = customtkinter.CTkCheckBox(self.Middle_frame,width=25,height=25, text="Add another File")
        self.Multi_Files.place(relx=0.87, rely=0.2, anchor=tkinter.CENTER)

        self.Backup_Button = customtkinter.CTkButton(self.Middle_frame, text="Start Backup", width=170, height=50)
        self.Backup_Button.place(relx=0.87, rely=0.9, anchor=tkinter.CENTER)

        self.Zip_The_File = customtkinter.CTkCheckBox(self.Sub_frame, width=100, height=100, text="Compress File")
        self.Zip_The_File.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)

        self.Delete_Local_File = customtkinter.CTkCheckBox(self.Sub_frame, width=100, height=100, text="Delete the local files")
        self.Delete_Local_File.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)




