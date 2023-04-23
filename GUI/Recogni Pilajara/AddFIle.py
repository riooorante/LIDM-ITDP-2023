import customtkinter as ctk
from PIL import Image

class AddFile(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x820")
        self.title("Recogni Pilajara")


        self.container = ctk.CTkFrame(self, corner_radius=0)
        self.container.grid(row=0, column=0, padx=10, pady=35)

        self.LFrame()
        self.formFrame()

    def LFrame(self):
        self.leftFrame_pgform= ctk.CTkFrame(self.container, corner_radius=0, width=300)
        self.leftFrame_pgform.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.leftFrame_pgform.grid_rowconfigure(10, weight=1)

        self.Maintext = ctk.CTkLabel(self.leftFrame_pgform, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.Maintext.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.button1 = ctk.CTkButton(self.leftFrame_pgform, text="Main Page")
        self.button1.grid(row=5, column=1, padx=55, pady=(30, 10))

        self.button2 = ctk.CTkButton(self.leftFrame_pgform, text="Add Data", )
        self.button2.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.leftFrame_pgform, text="Scan", fg_color='red')
        self.mainButton.grid(row=7, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.leftFrame_pgform, text='Mode', variable=self.switchVari, onvalue=True, offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

    def formFrame(self):

        self.img = ctk.CTkImage(dark_image= Image.open('Resources/FormPhoto.png'))
        self.buttonpict = ctk.CTkButton(self.container, text='FOTO',height=300, width=300, corner_radius=20, image=self.img)
        self.buttonpict.grid(row=0, column=2, padx=110, pady=(1, 0))

        self.frameform = ctk.CTkFrame(self.container,width=700, height=750, corner_radius=0)
        self.frameform.grid(row=0, column=3, rowspan=1, padx=0)
        self.frameform.grid_rowconfigure(10, weight=1)
        self.frameform.grid_propagate(0)

        self.form = ctk.CTkFrame(self.frameform,width=640, height=500, corner_radius=20)
        self.form.grid(row=2, column=1, rowspan=1, padx=30, pady=100, sticky="ns")
        self.form.grid_rowconfigure(10, weight=1)
        self.form.grid_propagate(0)

        self.nameLabel = ctk.CTkLabel(self.form, text="Nama")
        self.nameLabel.grid(row=2, column=1, columnspan=2,  padx=20, pady=10, sticky="w")

        self.nameEntry = ctk.CTkEntry(self.form, placeholder_text="Nama", width=400)
        self.nameEntry.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimLabel = ctk.CTkLabel(self.form, text="NIM")
        self.nimLabel.grid(row=4, column=1, columnspan=2,  padx=20, pady=10, sticky="w")

        self.nimEntry = ctk.CTkEntry(self.form, placeholder_text="NIM", width=400)
        self.nimEntry.grid(row=5, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.genderVar = ctk.StringVar(value="Prefer\not to say")
        self.genderLabel = ctk.CTkLabel(self.form, text="Jenis Kelamin")
        self.genderLabel.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        self.maleRadioButton = ctk.CTkRadioButton(self.form, text="Laki-Laki", variable=self.genderVar, value="He is")
        self.maleRadioButton.grid(row=6, column=2, padx=20, pady=10, sticky="w")

        self.femaleRadioButton = ctk.CTkRadioButton(self.form, text="Perempuan", variable=self.genderVar, value="She is")
        self.femaleRadioButton.grid(row=6, column=3, padx=20, pady=10, sticky="w")

        self.occupationLabel = ctk.CTkLabel(self.form, text="Program Studi")
        self.occupationLabel.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        self.occupationOptionMenu = ctk.CTkOptionMenu(self.form, values=["Sistem Informasi", "Matematika", "Fisika", "Kimia", "Biologi"])
        self.occupationOptionMenu.grid(row=7, column=2, padx=20, pady=10, columnspan=2, sticky="w")

        self.saveButton = ctk.CTkButton(self.frameform, height=60, width=200, corner_radius=10, text='SAVE', font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.saveButton.grid(row=3, columns =20, padx=10)

app = AddFile()
app.mainloop()