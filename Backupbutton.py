import customtkinter
import tkinter
from zipfile import ZipFile
import os

class Backupbutton:
    def BackupB(self,backup):
        self. backup = backup
        Filepath1 = self.backup.File_entry1.get()
        self.File_path1 = Filepath1

        backup.Middle_frame = customtkinter.CTkFrame(backup, width=850, height=500, corner_radius=10)
        backup.Middle_frame.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)
        backup.Sub_frame = customtkinter.CTkFrame(backup.Middle_frame, width=550, height=200, corner_radius=10)
        backup.Sub_frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        backup.File_entry1 = customtkinter.CTkEntry(backup.Middle_frame, width=450,height=25,corner_radius=10, placeholder_text="File Path")
        backup.File_entry1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        backup.Multi_Files = customtkinter.CTkButton(backup.Middle_frame,width=25,height=25, text="Add another File", command= self.ADDFile)
        backup.Multi_Files.place(relx=0.87, rely=0.2, anchor=tkinter.CENTER)

        backup.Backup_Button = customtkinter.CTkButton(backup.Middle_frame, text="Start Backup", width=170, height=50, command=self.ZIPFile)
        backup.Backup_Button.place(relx=0.87, rely=0.9, anchor=tkinter.CENTER)

        backup.Zip_The_File = customtkinter.CTkCheckBox(backup.Sub_frame, width=100, height=100, text="Compress File")
        backup.Zip_The_File.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)

        backup.Delete_Local_File = customtkinter.CTkCheckBox(backup.Sub_frame, width=100, height=100, text="Delete the local files")
        backup.Delete_Local_File.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)
    def ADDFile(self):
        Filepath2 = self.backup.File_entry2.get()
        self.File_path2 = Filepath2

        self.backup.File_entry2 = customtkinter.CTkEntry(self.backup.Middle_frame, width=450, height=25, corner_radius=10,placeholder_text="File Path")
        self.backup.File_entry2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    def ZIPFile(self):
        with ZipFile(self.File_path1,"w") as newzip:





