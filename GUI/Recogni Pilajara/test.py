import customtkinter as ctk
import tkinter as tk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1500x820")
        self.title("Recogni Pilajara")


        # Main Page
        self.mainpage = ctk.CTkFrame(self)
        self.mainpage.grid(row=0, column=0, sticky="nsew")

        self.Lframe_pgmain = ctk.CTkFrame(self.mainpage, corner_radius=0, width=300)
        self.Lframe_pgmain.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.Lframe_pgmain.grid_rowconfigure(10, weight=1)

        self.mainLabel = ctk.CTkLabel(self.Lframe_pgmain, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.Addbutton = ctk.CTkButton(self.Lframe_pgmain, text="Main Page")
        self.Addbutton.grid(row=5, column=1, padx=55, pady=(30, 10))

        self.scanButton = ctk.CTkButton(self.Lframe_pgmain, text="Add Data", command=self.addPage())
        self.scanButton.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.Lframe_pgmain, text="Scan", fg_color='red')
        self.mainButton.grid(row=7, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.Lframe_pgmain, text='Mode', variable=self.switchVari, onvalue=True,offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

        self.video = ctk.CTkButton(self.mainpage, width=640, height=480)
        self.video.grid(row=0, column=2, rowspan=4, sticky="w", padx=85)

        self.Rframe_pgmain = ctk.CTkFrame(self.mainpage, corner_radius=0, width=500)
        self.Rframe_pgmain.grid(row=0, column=4, rowspan=4, sticky="nsew")
        self.Rframe_pgmain.grid_rowconfigure(10, weight=1)

        self.foto = tk.Canvas(self.Rframe_pgmain, height=200, width=200)
        self.foto.grid(row=0, column=0, padx=120, pady=20, sticky='w')
        self.foto.grid_propagate(0)

        self.nama = ctk.CTkLabel(master=self.Rframe_pgmain, text="MARIO",font=ctk.CTkFont(family='Davish', size=70, weight='bold'))
        self.nama.grid(row=1, column=0, padx=106, pady=10, sticky='w')

        self.sum_label = ctk.CTkLabel(master=self.Rframe_pgmain, text='16',font=ctk.CTkFont(family='Davish', size=200, weight='bold'))
        self.sum_label.grid(row=2, column=0, padx=100, pady=(10, 12), sticky='w')

        self.mainButton = ctk.CTkButton(master=self.Rframe_pgmain, text='KEHADIRAN', font=ctk.CTkFont(family='Davish', size=30, weight='bold'), hover=False)
        self.mainButton.grid(row=10, column=0, padx=125, pady=1, sticky='w')

        # second Frame
        self.second_frame = ctk.CTkFrame(self)
        self.second_frame.grid(row=0, column=0, sticky="nsew")

        self.leftFrame_pgform = ctk.CTkFrame(self.second_frame, corner_radius=0, width=300)
        self.leftFrame_pgform.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.leftFrame_pgform.grid_rowconfigure(10, weight=1)

        self.Maintext = ctk.CTkLabel(self.leftFrame_pgform, text="RecogniPilajara",font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.Maintext.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.button1 = ctk.CTkButton(self.leftFrame_pgform, text="Main Page", command=self.mainPage())
        self.button1.grid(row=5, column=1, padx=55, pady=(30, 10))

        self.button2 = ctk.CTkButton(self.leftFrame_pgform, text="Add Data", )
        self.button2.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.leftFrame_pgform, text="Scan", fg_color='red')
        self.mainButton.grid(row=7, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.leftFrame_pgform, text='Mode', variable=self.switchVari, onvalue=True, offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

        self.buttonpict = ctk.CTkButton(self.second_frame, height=300, width=300, corner_radius=20)
        self.buttonpict.grid(row=0, column=2, padx=110, pady=(1, 0))

        self.frameform = ctk.CTkFrame(self.second_frame, width=700, height=750, corner_radius=10)
        self.frameform.grid(row=0, column=3, rowspan=1, padx=5)
        self.frameform.grid_rowconfigure(10, weight=1)
        self.frameform.grid_propagate(0)

        self.form = ctk.CTkFrame(self.frameform, width=640, height=500, corner_radius=20)
        self.form.grid(row=0, column=1, rowspan=1, padx=30, pady=100, sticky="ns")
        self.form.grid_rowconfigure(10, weight=1)
        self.form.grid_propagate(0)

        self.nameLabel = ctk.CTkLabel(self.form, text="Nama")
        self.nameLabel.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nameEntry = ctk.CTkEntry(self.form, placeholder_text="Nama", width=400)
        self.nameEntry.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimLabel = ctk.CTkLabel(self.form, text="NIM")
        self.nimLabel.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimEntry = ctk.CTkEntry(self.form, placeholder_text="NIM", width=400)
        self.nimEntry.grid(row=4, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.genderVar = ctk.StringVar(value="Prefer\not to say")
        self.genderLabel = ctk.CTkLabel(self.form, text="Jenis Kelamin")
        self.genderLabel.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        self.maleRadioButton = ctk.CTkRadioButton(self.form, text="Laki-Laki", variable=self.genderVar, value="He is")
        self.maleRadioButton.grid(row=5, column=2, padx=20, pady=10, sticky="w")

        self.femaleRadioButton = ctk.CTkRadioButton(self.form, text="Perempuan", variable=self.genderVar,value="She is")
        self.femaleRadioButton.grid(row=5, column=3, padx=20, pady=10, sticky="w")

        self.occupationLabel = ctk.CTkLabel(self.form, text="Program Studi")
        self.occupationLabel.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        self.occupationOptionMenu = ctk.CTkOptionMenu(self.form,values=["Sistem Informasi", "Matematika", "Fisika", "Kimia","Biologi"])
        self.occupationOptionMenu.grid(row=6, column=2, padx=20, pady=10, columnspan=2, sticky="w")


        self.mainpage()

    def mainPage(self):
        self.second_frame.grid_forget()
        self.mainpage.grid(row=0, columns=0, sticky='nsew')

    def addPage(self):
        self.mainpage.grid_forget()
        self.second_frame.grid(row=0, columns=0, sticky='nsew')

if __name__ == '__main__':
    app = App()
    app.mainloop()

