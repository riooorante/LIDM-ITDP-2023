import customtkinter as ctk
import tkinter as tk

window = ctk.CTk()
window.geometry("1500x820")
window.title("Recogni Pilajara")
window.rowconfigure(0, weight=1)

frameKiri = ctk.CTkFrame(window, corner_radius=0, width=300)
frameKiri.grid(row=0, column=1, rowspan=4, sticky="nsew")
frameKiri.grid_rowconfigure(10, weight=1)

mainLabel = ctk.CTkLabel(frameKiri, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

button = ctk.CTkButton(frameKiri, text="Add Data")
button.grid(row=5, column=1, padx=55, pady=(30, 10))

button = ctk.CTkButton(frameKiri, text="Scan", )
button.grid(row=6, column=1, padx=55, pady=(30, 10))

button = ctk.CTkOptionMenu(frameKiri, values=["Indonesia", "English"])
button.grid(row=7, column=1, padx=55, pady=(30, 10))

switchVari = ctk.BooleanVar(value=True)
switch_1 = ctk.CTkSwitch(frameKiri, text='Mode', variable=switchVari, onvalue=True, offvalue=False)
switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

video = tk.Canvas(window, bg='black', height=480, width=640)
video.grid(row=0, column=2, padx=25, pady=(20, 0))

frameKanan = ctk.CTkFrame(window, corner_radius=0, width=600)
frameKanan.grid(row=0, column=3, rowspan=4, sticky="nsew")
frameKanan.grid_rowconfigure(15, weight=1)

foto = tk.Canvas(frameKanan, bg='black', height=200, width=200)
foto.grid(row=0, column=1, padx=0, pady=(30, 0)) # padx ->135

nama = ctk.CTkLabel(frameKanan, text="Mario".capitalize(), font=ctk.CTkFont(family='Davish', size=30, weight='bold'))
nama.grid(row=1, column=1, padx=120, pady=(90, 0))

labelHadir = ctk.CTkLabel(frameKanan, text="16", font=ctk.CTkFont(family='Davish', size=190, weight='bold'))
labelHadir.grid(row=3, column=1, padx=12, pady=(130, 0))

labelHadir1 = ctk.CTkLabel(frameKanan, text="KEHADIRAN", font=ctk.CTkFont(family='Davish', size=30, weight='bold'))
labelHadir1.grid(row=4, column=1, padx=120, pady=(120, 0))


window.mainloop()
