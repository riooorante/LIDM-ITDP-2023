import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

window = ctk.CTk()
window.geometry("1500x820")
window.title("Recogni Pilajara")
window.rowconfigure(0, weight=1)

frameKiri = ctk.CTkFrame(window, corner_radius=10, width=300)
frameKiri.grid(row=0, column=2, rowspan=4, sticky = "nsew")
frameKiri.grid_rowconfigure(10, weight=1)

mainLabel = ctk.CTkLabel(frameKiri, text="RecogniPilajara", font=ctk.CTkFont(family='Davish',size=20, weight='bold'))
mainLabel.grid(row=1, column=1, padx=55, pady=(30,10))

button = ctk.CTkButton(frameKiri, text="Add Data")
button.grid(row=5, column=1, padx=55, pady=(30,10))

button = ctk.CTkButton(frameKiri, text="Scan", )
button.grid(row=6, column=1, padx=55, pady=(30,10))

button = ctk.CTkOptionMenu(frameKiri, values=["Indonesia", "English"])
button.grid(row=7, column=1, padx=55, pady=(30,10))

switch_1 = ctk.CTkSwitch(frameKiri, text='Mode', onvalue="on", offvalue="off")
switch_1.grid(row=13, column=1, padx=55, pady=(30,10))

video = tk.Canvas(window, bg='black', height=480, width=640)
video.grid(row=0, column=5, padx=65, pady=(20,0))

frameKanan = ctk.CTkFrame(window, corner_radius=10, width=600)
frameKanan.grid(row=0, column=7, rowspan=4, sticky = "nsew")
frameKanan.grid_rowconfigure(10, weight=1)

foto = tk.Canvas(frameKanan, bg='black', height=200, width=200)
foto.grid(row=0, column=1, padx=140, pady=(20,0))


window.mainloop()