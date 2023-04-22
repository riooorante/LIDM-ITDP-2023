import customtkinter as ctk

class AddFile():

    def __init__(self):
        self.window = ctk.CTk()
    def mainpage1(self):
        window.geometry("1500x820")
        window.title("Recogni Pilajara")
        window.rowconfigure(0, weight=1)

frameKiri = ctk.CTkFrame(window, corner_radius=0, width=300)
frameKiri.grid(row=0, column=1, rowspan=4, sticky="nsew")
frameKiri.grid_rowconfigure(10, weight=1)

mainLabel = ctk.CTkLabel(frameKiri, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

button1 = ctk.CTkButton(frameKiri, text="Add Data")
button1.grid(row=5, column=1, padx=55, pady=(30, 10))

button2 = ctk.CTkButton(frameKiri, text="Scan", )
button2.grid(row=6, column=1, padx=55, pady=(30, 10))

button3 = ctk.CTkOptionMenu(frameKiri, values=["Indonesia", "English"])
button3.grid(row=7, column=1, padx=55, pady=(30, 10))

switchVari = ctk.BooleanVar(value=True)
switch_1 = ctk.CTkSwitch(frameKiri, text='Mode', variable=switchVari, onvalue=True, offvalue=False)
switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

buttonpict = ctk.CTkButton(window, height=300, width=300, corner_radius=20)
buttonpict.grid(row=0, column=2, padx=65, pady=(1, 0))

frameform = ctk.CTkFrame(window,width=700, height=750, corner_radius=0)
frameform.grid(row=0, column=3, rowspan=1)
frameform.grid_rowconfigure(10, weight=1)
frameform.grid_propagate(0)

form = ctk.CTkFrame(frameform,width=640, height=500, corner_radius=20)
form.grid(row=0, column=1, rowspan=1, padx=20, pady=100, sticky="ns")
form.grid_rowconfigure(10, weight=1)
form.grid_propagate(0)

nameLabel = ctk.CTkLabel(form, text="Nama")
nameLabel.grid(row=1, column=1, columnspan=2,  padx=20, pady=10, sticky="w")

nameEntry = ctk.CTkEntry(form, placeholder_text="Nama", width=400)
nameEntry.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="w")

nimLabel = ctk.CTkLabel(form, text="NIM")
nimLabel.grid(row=3, column=1, columnspan=2,  padx=20, pady=10, sticky="w")

nimEntry = ctk.CTkEntry(form, placeholder_text="NIM", width=400)
nimEntry.grid(row=4, column=1, columnspan=2, padx=20, pady=10, sticky="w")

genderVar = ctk.StringVar(value="Prefer\not to say")
genderLabel = ctk.CTkLabel(form, text="Jenis Kelamin")
genderLabel.grid(row=5, column=1, padx=20, pady=10, sticky="w")

maleRadioButton = ctk.CTkRadioButton(form, text="Laki-Laki", variable=genderVar, value="He is")
maleRadioButton.grid(row=5, column=2, padx=20, pady=10, sticky="w")

femaleRadioButton = ctk.CTkRadioButton(form, text="Perempuan", variable=genderVar, value="She is")
femaleRadioButton.grid(row=5, column=3, padx=20, pady=10, sticky="w")

occupationLabel = ctk.CTkLabel(form, text="Program Studi")
occupationLabel.grid(row=6, column=1, padx=20, pady=10, sticky="w")

occupationOptionMenu = ctk.CTkOptionMenu(form, values=["Sistem Informasi", "Matematika", "Fisika", "Kimia", "Biologi"])
occupationOptionMenu.grid(row=6, column=2, padx=20, pady=10, columnspan=2, sticky="w")



window.mainloop()
