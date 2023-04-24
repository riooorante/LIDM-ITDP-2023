import customtkinter as ctk
import tkinter as tk
from PIL import Image


class AddFile(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x820")
        self.title("Recogni Pilajara")

        self.container_mainpage = ctk.CTkFrame(self, corner_radius=0)
        self.container_formpage = ctk.CTkFrame(self, corner_radius=0)

        self.show_Mainpage()

    def LFrame_Formpage(self):
        self.leftFrame_pgform = ctk.CTkFrame(self.container_formpage, corner_radius=0, width=300)
        self.leftFrame_pgform.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.leftFrame_pgform.grid_rowconfigure(10, weight=1)

        self.Maintext = ctk.CTkLabel(self.leftFrame_pgform, text="RecogniPilajara",
                                     font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.Maintext.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.button1 = ctk.CTkButton(self.leftFrame_pgform, text="Main Page", command=self.show_Mainpage())
        self.button1.grid(row=5, column=1, padx=55, pady=(30, 10))

        self.button2 = ctk.CTkButton(self.leftFrame_pgform, text="Add Data", )
        self.button2.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.leftFrame_pgform, text="Scan", fg_color='red')
        self.mainButton.grid(row=7, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.leftFrame_pgform, text='Mode', variable=self.switchVari, onvalue=True,
                                      offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

    def formFrame_Formpage(self):
        self.img = ctk.CTkImage(dark_image=Image.open('Resources/FormPhoto.png'))
        self.buttonpict = ctk.CTkButton(self.container_formpage, text='FOTO', height=300, width=300, corner_radius=20,
                                        image=self.img)
        self.buttonpict.grid(row=0, column=2, padx=110, pady=(1, 0))

        self.frameform = ctk.CTkFrame(self.container_formpage, width=700, height=750, corner_radius=0)
        self.frameform.grid(row=0, column=3, rowspan=1, padx=0)
        self.frameform.grid_rowconfigure(10, weight=1)
        self.frameform.grid_propagate(0)

        self.form = ctk.CTkFrame(self.frameform, width=640, height=500, corner_radius=20)
        self.form.grid(row=2, column=1, rowspan=1, padx=30, pady=100, sticky="ns")
        self.form.grid_rowconfigure(10, weight=1)
        self.form.grid_propagate(0)

        self.nameLabel = ctk.CTkLabel(self.form, text="Nama")
        self.nameLabel.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nameEntry = ctk.CTkEntry(self.form, placeholder_text="Nama", width=400)
        self.nameEntry.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimLabel = ctk.CTkLabel(self.form, text="NIM")
        self.nimLabel.grid(row=4, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimEntry = ctk.CTkEntry(self.form, placeholder_text="NIM", width=400)
        self.nimEntry.grid(row=5, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.genderVar = ctk.StringVar(value="Prefer\not to say")
        self.genderLabel = ctk.CTkLabel(self.form, text="Jenis Kelamin")
        self.genderLabel.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        self.maleRadioButton = ctk.CTkRadioButton(self.form, text="Laki-Laki", variable=self.genderVar, value="He is")
        self.maleRadioButton.grid(row=6, column=2, padx=20, pady=10, sticky="w")

        self.femaleRadioButton = ctk.CTkRadioButton(self.form, text="Perempuan", variable=self.genderVar,
                                                    value="She is")
        self.femaleRadioButton.grid(row=6, column=3, padx=20, pady=10, sticky="w")

        self.occupationLabel = ctk.CTkLabel(self.form, text="Program Studi")
        self.occupationLabel.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        self.occupationOptionMenu = ctk.CTkOptionMenu(self.form,
                                                      values=["Sistem Informasi", "Matematika", "Fisika", "Kimia",
                                                              "Biologi"])
        self.occupationOptionMenu.grid(row=7, column=2, padx=20, pady=10, columnspan=2, sticky="w")

        self.saveButton = ctk.CTkButton(self.frameform, height=60, width=200, corner_radius=10, text='SAVE',
                                        font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.saveButton.grid(row=3, columns=20, padx=10)

    def Lframe_mainpage(self):
        self.Lframe_pgmain = ctk.CTkFrame(self.container_mainpage, corner_radius=0, width=300)
        self.Lframe_pgmain.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.Lframe_pgmain.grid_rowconfigure(10, weight=1)

        self.mainLabel = ctk.CTkLabel(self.Lframe_pgmain, text="RecogniPilajara",
                                      font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.Addbutton = ctk.CTkButton(self.Lframe_pgmain, text="Main Page")
        self.Addbutton.grid(row=5, column=1, padx=55, pady=(30, 10))

        self.scanButton = ctk.CTkButton(self.Lframe_pgmain, text="Add Data", command=self.show_Formpage())
        self.scanButton.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.Lframe_pgmain, text="Scan", fg_color='red')
        self.mainButton.grid(row=7, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.Lframe_pgmain, text='Mode', variable=self.switchVari, onvalue=True,
                                      offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

    def center_mainpage(self):
        self.video = ctk.CTkButton(self.container_mainpage, width=640, height=480)
        self.video.grid(row=0, column=2, rowspan=4, sticky="w", padx=85)

    def Rframe_mainpage(self):
        self.Rframe_pgmain = ctk.CTkFrame(self.container_mainpage, corner_radius=0, width=500)
        self.Rframe_pgmain.grid(row=0, column=4, rowspan=4, sticky="nsew")
        self.Rframe_pgmain.grid_rowconfigure(10, weight=1)

        self.foto = tk.Canvas(self.Rframe_pgmain, height=200, width=200)
        self.foto.grid(row=0, column=0, padx=120, pady=20, sticky='w')
        self.foto.grid_propagate(0)

        self.nama = ctk.CTkLabel(master=self.Rframe_pgmain, text="MARIO",
                                 font=ctk.CTkFont(family='Davish', size=70, weight='bold'))
        self.nama.grid(row=1, column=0, padx=106, pady=10, sticky='w')

        self.sum_label = ctk.CTkLabel(master=self.Rframe_pgmain, text='16',
                                      font=ctk.CTkFont(family='Davish', size=200, weight='bold'))
        self.sum_label.grid(row=2, column=0, padx=100, pady=(10, 12), sticky='w')

        self.mainButton = ctk.CTkButton(master=self.Rframe_pgmain, text='KEHADIRAN',
                                        font=ctk.CTkFont(family='Davish', size=30, weight='bold'), hover=False)
        self.mainButton.grid(row=10, column=0, padx=125, pady=1, sticky='w')

    def show_Formpage(self):
        if self.scanButton:
            self.container_mainpage.grid_forget()
            self.container_formpage.grid(row=0, column=0, padx=10, pady=35)
            self.LFrame_Formpage()
            self.formFrame_Formpage()
        self.scanButton = False

    def show_Mainpage(self):
        if self.button1:
            self.container_formpage.grid_forget()
            self.container_mainpage.grid(row=0, column=0, padx=10, pady=35)
            self.Lframe_mainpage()
            self.center_mainpage()
            self.Rframe_mainpage()
        self.button1 = False


app = AddFile()
app.show_Mainpage()
