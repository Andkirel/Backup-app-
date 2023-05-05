import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #logo, title and window size
        self.title("Guardian")
        self.geometry("1100x580")
        self.iconbitmap("App-logo.ICO")

        #Main grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.App_Name_label = customtkinter.CTkLabel(self, text="Guardian", font=customtkinter.CTkFont(size=45, weight="bold"))
        self.App_Name_label.grid(row=3, column=3, padx=20, pady=(20, 10))

#Side Menu
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
#Side Menu label
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
#Side Menu buttons
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Backup", command=self.Backup_button_event1)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Create User ID", command=self.CUID_button_event2)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Help", command=self.Help_button_event3)
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)
#Side Menu OptionMenu's
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,values=["Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def Backup_button_event1(self):
        self.Middle_frame = customtkinter.CTkFrame(self, width=850,height=500,corner_radius=10)
        self.Middle_frame.grid(row = 0,column=3,sticky = "" )
        #self.File_Path = customtkinter.CTkEntry(self.Middle_frame,width=700,height=24, corner_radius=10)
        #self.File_Path .grid(row=1, column=0, padx=20, pady=10)



    def CUID_button_event2(self):
        print("Create User ID")

    def Help_button_event3(self):
        print("Help")



if __name__ == "__main__":
    app = App()
    app.mainloop()

