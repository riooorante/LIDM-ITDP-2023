import customtkinter as ctk

class AddFile():

    def __init__(self):
        self.window = ctk.CTk()
    def mainpage1(self):
        self.window.geometry("1500x820")
        self.window.title("Recogni Pilajara")
        self.window.rowconfigure(0, weight=1)

        self.LFrame()
        self.formFrame()
        self.window.mainloop()

    def LFrame(self):
        self.leftFrame_pgform= ctk.CTkFrame(self.window, corner_radius=0, width=300)
        self.leftFrame_pgform.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.leftFrame_pgform.grid_rowconfigure(10, weight=1)

        self.Maintext = ctk.CTkLabel(self.leftFrame_pgform
                , text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.Maintext.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.button1 = ctk.CTkButton(self.leftFrame_pgform
            , text="Add Data")
        self.button1.grid(row=5, column=1, padx=55, pady=(30, 10))

        self.button2 = ctk.CTkButton(self.leftFrame_pgform
            , text="Add Data", )
        self.button2.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.leftFrame_pgform, text="Scan", fg_color='red')
        self.mainButton.grid(row=7, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.leftFrame_pgform
                , text='Mode', variable=self.switchVari, onvalue=True, offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

    def formFrame(self):

        self.buttonpict = ctk.CTkButton(self.window, height=300, width=300, corner_radius=20)
        self.buttonpict.grid(row=0, column=2, padx=110, pady=(1, 0))

        self.frameform = ctk.CTkFrame(self.window,width=700, height=750, corner_radius=10)
        self.frameform.grid(row=0, column=3, rowspan=1, padx=5)
        self.frameform.grid_rowconfigure(10, weight=1)
        self.frameform.grid_propagate(0)

        self.form = ctk.CTkFrame(self.frameform,width=640, height=500, corner_radius=20)
        self.form.grid(row=0, column=1, rowspan=1, padx=30, pady=100, sticky="ns")
        self.form.grid_rowconfigure(10, weight=1)
        self.form.grid_propagate(0)

        self.nameLabel = ctk.CTkLabel(self.form, text="Nama")
        self.nameLabel.grid(row=1, column=1, columnspan=2,  padx=20, pady=10, sticky="w")

        self.nameEntry = ctk.CTkEntry(self.form, placeholder_text="Nama", width=400)
        self.nameEntry.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimLabel = ctk.CTkLabel(self.form, text="NIM")
        self.nimLabel.grid(row=3, column=1, columnspan=2,  padx=20, pady=10, sticky="w")

        self.nimEntry = ctk.CTkEntry(self.form, placeholder_text="NIM", width=400)
        self.nimEntry.grid(row=4, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.genderVar = ctk.StringVar(value="Prefer\not to say")
        self.genderLabel = ctk.CTkLabel(self.form, text="Jenis Kelamin")
        self.genderLabel.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        self.maleRadioButton = ctk.CTkRadioButton(self.form, text="Laki-Laki", variable=self.genderVar, value="He is")
        self.maleRadioButton.grid(row=5, column=2, padx=20, pady=10, sticky="w")

        self.femaleRadioButton = ctk.CTkRadioButton(self.form, text="Perempuan", variable=self.genderVar, value="She is")
        self.femaleRadioButton.grid(row=5, column=3, padx=20, pady=10, sticky="w")

        self.occupationLabel = ctk.CTkLabel(self.form, text="Program Studi")
        self.occupationLabel.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        self.occupationOptionMenu = ctk.CTkOptionMenu(self.form, values=["Sistem Informasi", "Matematika", "Fisika", "Kimia", "Biologi"])
        self.occupationOptionMenu.grid(row=6, column=2, padx=20, pady=10, columnspan=2, sticky="w")

app = AddFile()
app.mainpage1()