import customtkinter as ctk
import tkinter as tk

window = ctk.CTk()
window.geometry("1500x820")
window.title("Recogni Pilajara")
window.rowconfigure(0, weight=1)

frameKiri = ctk.CTkFrame(window, corner_radius=0, width=300)
frameKiri.grid(row=0, column=2, rowspan=4, sticky="nsew")
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
buttonpict.grid(row=0, column=6, padx=65, pady=(1, 0))

window.mainloop()
