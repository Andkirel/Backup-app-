import customtkinter
import tkinter
from zipfile import ZipFile
import pathlib

class Backupbutton:
    def BackupB(self,backup):
        self.backup = backup

        backup.Middle_frame = customtkinter.CTkFrame(backup, width=850, height=500, corner_radius=10)
        backup.Middle_frame.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)
        backup.Sub_frame = customtkinter.CTkFrame(backup.Middle_frame, width=550, height=200, corner_radius=10)
        backup.Sub_frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        backup.File_entry1 = customtkinter.CTkEntry(backup.Middle_frame, width=450,height=25,corner_radius=10, placeholder_text="File Path")
        backup.File_entry1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        backup.File_entry2 = customtkinter.CTkEntry(backup.Middle_frame, width=450, height=25,corner_radius=10, placeholder_text="File Path")
        backup.File_entry2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        backup.Backup_Button = customtkinter.CTkButton(backup.Middle_frame, text="Start Backup", width=170, height=50, command=self.ZIPFile)
        backup.Backup_Button.place(relx=0.87, rely=0.9, anchor=tkinter.CENTER)

        backup.LABEL = customtkinter.CTkLabel(backup.Sub_frame, text="Account data will be stored in", anchor="w",font=customtkinter.CTkFont(size=24, weight="bold"))
        backup.LABEL.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        backup.USER = customtkinter.CTkEntry(backup.Sub_frame, width=250, height=25, placeholder_text="Username")
        backup.USER.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        backup.PIN = customtkinter.CTkEntry(backup.Sub_frame, width=250, height=25, placeholder_text="PIN")
        backup.PIN.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def ZIPFile(self):

        Filepath1 = self.backup.File_entry1.get()
        Filepath2 = self.backup.File_entry2.get()

        self.File_path1 = Filepath1
        self.File_path2 = Filepath2

        with ZipFile('backup.zip','w') as zip:
         for folder in [self.File_path1, self.File_path2]:
             for file in pathlib.Path(folder).iterdir():
              zip.write(file)