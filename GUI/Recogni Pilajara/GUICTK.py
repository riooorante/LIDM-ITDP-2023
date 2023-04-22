import customtkinter as ctk
import tkinter as tk
from Scanner import WebcamCapture
import threading

window = ctk.CTk()
window.geometry("1500x820")
window.title("Recogni Pilajara")
window.rowconfigure(0, weight=1)

Lframe_PgMain = ctk.CTkFrame(window, corner_radius=0, width=300)
Lframe_PgMain.grid(row=0, column=1, rowspan=4, sticky="nsew")
Lframe_PgMain.grid_rowconfigure(10, weight=1)

mainLabel = ctk.CTkLabel(Lframe_PgMain, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

Addbutton = ctk.CTkButton(Lframe_PgMain, text="Add Data")
Addbutton.grid(row=5, column=1, padx=55, pady=(30, 10))

scanButton = ctk.CTkButton(Lframe_PgMain, text="Scan", )
scanButton.grid(row=6, column=1, padx=55, pady=(30, 10))

mainButton = ctk.CTkButton(Lframe_PgMain, text="Main Page", )
mainButton.grid(row=6, column=1, padx=55, pady=(30, 10))

switchVari = ctk.BooleanVar(value=True)
switch_1 = ctk.CTkSwitch(Lframe_PgMain, text='Mode', variable=switchVari, onvalue=True, offvalue=False)
switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

camlabel = ctk.CTkLabel(window)
camlabel.grid(row=0, column=2, padx=25, pady=(20, 0))

webcam = WebcamCapture(camlabel)
webcam.start()
print("WEBCAM START")

Rframe_pgmain = ctk.CTkFrame(window, corner_radius=0, width=600)
Rframe_pgmain.grid(row=0, column=4, rowspan=4, sticky="nsew")
Rframe_pgmain.grid_rowconfigure(10, weight=1)

foto = tk.Canvas(Rframe_pgmain, height=200,width=200)
foto.grid(row=0, column=0, padx=120, pady=20, sticky='w')
foto.grid_propagate(0)

nama = ctk.CTkLabel(master=Rframe_pgmain, text="MARIO",font=ctk.CTkFont(family='Davish', size=70, weight='bold'))
nama.grid(row=1, column=0, padx=106, pady=10, sticky='w')

sum_label = ctk.CTkLabel(master=Rframe_pgmain, text='16',font=ctk.CTkFont(family='Davish', size=200, weight='bold'))
sum_label.grid(row=2, column=0, padx=100, pady=(10,12), sticky='w')

mainButton = ctk.CTkButton(master=Rframe_pgmain, text='KEHADIRAN', font=ctk.CTkFont(family='Davish', size=30, weight='bold'),hover=False)
mainButton.grid(row=10, column=0, padx=140, pady=1, sticky='w')

def on_closing():
    # Stop and release webcam capture before closing window
    webcam.stop()
    webcam.release()
    print("WEBCAM END")
    window.quit()

t = threading.Thread(target=on_closing)

window.protocol("WM_DELETE_WINDOW", lambda: t.start())

window.mainloop()
