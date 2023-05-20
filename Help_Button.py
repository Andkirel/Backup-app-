import customtkinter
import tkinter

class Help_Button:

    def helpB(self, help):
        self.help = help

        help.Middle_frame = customtkinter.CTkFrame(help, width=850, height=500, corner_radius=10)
        help.Middle_frame.place(relx=0.585, rely=0.45, anchor=tkinter.CENTER)

        help.textbox = customtkinter.CTkTextbox(help.Middle_frame, width=850, height=500, corner_radius=10)
        help.textbox.grid(row=0, column=0, sticky="nsew")
        help.textbox.insert("0.0", "Thank you, for choosing Guardian for your file transfer needs! Please see below for instructions on how Guardian works\n\n1: Create a User ID and PIN, if you click on the second button labeled “Create User ID” it will display 3 entry fields where you will need to enter your Username, pin, and confirm pin. Once you have entered the information please confirm its correct and click “Submit” this will create your account.\n\n2: Now that your account is created please select the first button labeled “Backup” this will display an entry filed and some options, please inspect the options and make your selections. If you require more then 1 file you can add a second entry field by selecting the check box labeled “Add another File \n\nNOTE: if you have more then 2 files needing to be moved please put all files in a single folder on the desktop and add that folders file path to the entry field instead\n\n3:Open File Explorer and copy the file paths into the entry field.\n\n4: Click the button labeled “Start Backup” located at the bottom right of the application.\n\n5: A new Window will appear asking you for your User ID and pin enter the information and click submit.\n\nCongratulation’s you have completed your first file transfer to access the files you will need to go to the following file paths listed below.\n\n\nFile Paths: \n\nTBD\n\nTBD")
        help.text = help.textbox.get("0.0", "end")
        help.textbox.configure(state="disabled")
