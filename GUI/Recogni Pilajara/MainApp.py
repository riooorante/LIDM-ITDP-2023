import customtkinter as ctk
import tkinter as tk
import firebase_admin
import os
import shutil
from PIL import Image
from customtkinter import filedialog
from firebase_admin import credentials
from firebase_admin import db

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1500x820")
        self.title("Recogni Pilajara")

        self.mainPage = ctk.CTkFrame(self)
        self.second_frame = ctk.CTkFrame(self)

        # Main Page

        self.Lframe_pgmain = ctk.CTkFrame(self.mainPage, corner_radius=0, width=300)
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

        self.video = ctk.CTkButton(self.mainPage, width=640, height=480)
        self.video.grid(row=0, column=2, rowspan=4, sticky="w", padx=85)

        self.Rframe_pgmain = ctk.CTkFrame(self.mainPage, corner_radius=0, width=500)
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

        self.leftFrame_pgform = ctk.CTkFrame(self.second_frame, corner_radius=0, width=300)
        self.leftFrame_pgform.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.leftFrame_pgform.grid_rowconfigure(10, weight=1)

        self.Maintext = ctk.CTkLabel(self.leftFrame_pgform, text="RecogniPilajara",font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.Maintext.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.button1 = ctk.CTkButton(self.leftFrame_pgform, text="Main Page", command=self.main())
        self.button1.grid(row=5, column=1, padx=55, pady=(30, 10))

        self.button2 = ctk.CTkButton(self.leftFrame_pgform, text="Add Data", )
        self.button2.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.leftFrame_pgform, text="Scan", fg_color='red')
        self.mainButton.grid(row=7, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.leftFrame_pgform, text='Mode', variable=self.switchVari, onvalue=True, offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

        self.img = ctk.CTkImage(dark_image=Image.open('Resources/FormPhoto.png'))
        self.buttonpict = ctk.CTkButton(self.second_frame, text='FOTO', height=300, width=300, corner_radius=20,
                                        image=self.img, command=self.openPhoto())
        self.buttonpict.grid(row=0, column=2, padx=110, pady=(1, 0))

        self.frameform = ctk.CTkFrame(self.second_frame, width=700, height=750, corner_radius=0)
        self.frameform.grid(row=0, column=3, rowspan=1, padx=0)
        self.frameform.grid_rowconfigure(10, weight=1)
        self.frameform.grid_propagate(0)

        self.form = ctk.CTkFrame(self.frameform, width=640, height=500, corner_radius=20)
        self.form.grid(row=2, column=1, rowspan=1, padx=30, pady=100, sticky="ns")
        self.form.grid_rowconfigure(10, weight=1)
        self.form.grid_propagate(0)

        self.nameLabel = ctk.CTkLabel(self.form, text="Nama")
        self.nameLabel.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nameEntry = ctk.CTkEntry(self.form, placeholder_text="Nama", width=400, )
        self.nameEntry.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimLabel = ctk.CTkLabel(self.form, text="NIM")
        self.nimLabel.grid(row=4, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimEntry = ctk.CTkEntry(self.form, placeholder_text="NIM", width=400)
        self.nimEntry.grid(row=5, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.genderVar = ctk.StringVar(value="Prefer\not to say")
        self.genderLabel = ctk.CTkLabel(self.form, text="Jenis Kelamin")
        self.genderLabel.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        self.maleRadioButton = ctk.CTkRadioButton(self.form, text="Laki-Laki", variable=self.genderVar,
                                                  value="Laki-laki")
        self.maleRadioButton.grid(row=6, column=2, padx=20, pady=10, sticky="w")

        self.femaleRadioButton = ctk.CTkRadioButton(self.form, text="Perempuan", variable=self.genderVar,
                                                    value="Perempuan")
        self.femaleRadioButton.grid(row=6, column=3, padx=20, pady=10, sticky="w")

        self.majorVar = ctk.StringVar()
        self.occupationLabel = ctk.CTkLabel(self.form, text="Program Studi")
        self.occupationLabel.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        self.occupationOptionMenu = ctk.CTkOptionMenu(self.form, variable=self.majorVar,
                                                      values=["Sistem Informasi", "Matematika", "Fisika", "Kimia",
                                                              "Biologi"])
        self.occupationOptionMenu.grid(row=7, column=2, padx=20, pady=10, columnspan=2, sticky="w")

        self.saveButton = ctk.CTkButton(self.frameform, height=60, width=200, corner_radius=10, text='SAVE',
                                        font=ctk.CTkFont(family='Davish', size=20, weight='bold'),
                                        command=self.Save_data())
        self.saveButton.grid(row=3, columns=20, padx=10)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.mainPage.rowconfigure(0, weight=1)
        self.mainPage.columnconfigure(0, weight=1)
        self.mainPage.columnconfigure(1, weight=1)
        self.second_frame.rowconfigure(0, weight=1)
        self.second_frame.columnconfigure(0, weight=1)

        self.main()

    def main(self):
        self.second_frame.grid_forget()
        self.mainPage.grid(row=0, columns=1, sticky='nsew')

    def addPage(self):
        self.mainPage.grid_forget()
        self.second_frame.grid(row=0, columns=1, sticky='nsew')

    def Save_data(self):
        self.user_name = self.nameEntry.get()
        self.user_NIM = self.nimEntry.get()
        self.user_Gender = self.genderVar.get()
        self.user_Major = self.majorVar.get()

        self.cred = credentials.Certificate("path/to/serviceAccountKey.json")
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': "https://pilajara-d8d3f-default-rtdb.firebaseio.com"
        } )
        self.ref = db.reference('/')

        data = {
            'ID':self.user_NIM,
            'Major':self.user_Major,
            'Kehadiran':0,
            'LastScan':0,
            'Nama':self.user_name
        }

        self.ref.push(data)
    def openPhoto(self):
        self.sep = r"\"

        self.file_path = filedialog.askopenfilename()
        self.new_file_path = list(map(str, self.file_path.split(self.sep)))
        self.new_file_path[-1] = self.user_NIM

        self.new_file_path = os.rename(self.file_path, self.sep.join(self.new_file_path))
        self.destination = "D:\Programming\Project\LIDM-ITDP-2023\GUI\Recogni Pilajara\Profile"
        self.listOfdata = os.listdir(self.destination)

        if self.user_NIM not in self.listOfdata:
            shutil.copy(self.new_file_path, self.destination)


app = App()
app.mainloop()

