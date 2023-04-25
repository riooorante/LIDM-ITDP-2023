# import customtkinter as ctk
# import tkinter as tk
# from Scanner import WebcamCapture
# import threading
#
# window = ctk.CTk()
# window.geometry("1500x820")
# window.title("Recogni Pilajara")
# window.rowconfigure(0, weight=1)
#
# Lframe_PgMain = ctk.CTkFrame(window, corner_radius=0, width=300)
# Lframe_PgMain.grid(row=0, column=1, rowspan=4, sticky="nsew")
# Lframe_PgMain.grid_rowconfigure(10, weight=1)
#
# mainLabel = ctk.CTkLabel(Lframe_PgMain, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
# mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))
#
# Addbutton = ctk.CTkButton(Lframe_PgMain, text="Add Data")
# Addbutton.grid(row=5, column=1, padx=55, pady=(30, 10))
#
# scanButton = ctk.CTkButton(Lframe_PgMain, text="Scan", )
# scanButton.grid(row=6, column=1, padx=55, pady=(30, 10))
#
# mainButton = ctk.CTkButton(Lframe_PgMain, text="Main Page", )
# mainButton.grid(row=6, column=1, padx=55, pady=(30, 10))
#
# switchVari = ctk.BooleanVar(value=True)
# switch_1 = ctk.CTkSwitch(Lframe_PgMain, text='Mode', variable=switchVari, onvalue=True, offvalue=False)
# switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))
#
# camlabel = tk.Label(window)
# camlabel.grid(row=0, column=2, padx=25, pady=(20, 0))
#
# webcam = WebcamCapture(camlabel)
# webcam.start()
# print("WEBCAM START")
#
# Rframe_pgmain = ctk.CTkFrame(window, corner_radius=0, width=600)
# Rframe_pgmain.grid(row=0, column=4, rowspan=4, sticky="nsew")
# Rframe_pgmain.grid_rowconfigure(10, weight=1)
#
# foto = tk.Canvas(Rframe_pgmain, height=200,width=200)
# foto.grid(row=0, column=0, padx=120, pady=20, sticky='w')
# foto.grid_propagate(0)
#
# nama = ctk.CTkLabel(master=Rframe_pgmain, text="MARIO",font=ctk.CTkFont(family='Davish', size=70, weight='bold'))
# nama.grid(row=1, column=0, padx=106, pady=10, sticky='w')
#
# sum_label = ctk.CTkLabel(master=Rframe_pgmain, text='16',font=ctk.CTkFont(family='Davish', size=200, weight='bold'))
# sum_label.grid(row=2, column=0, padx=100, pady=(10,12), sticky='w')
#
# mainButton = ctk.CTkButton(master=Rframe_pgmain, text='KEHADIRAN', font=ctk.CTkFont(family='Davish', size=30, weight='bold'),hover=False)
# mainButton.grid(row=10, column=0, padx=140, pady=1, sticky='w')
#
# def on_closing():
#     # Stop and release webcam capture before closing window
#     webcam.stop()
#     webcam.release()
#     print("WEBCAM END")
#     window.quit()
#
# t = threading.Thread(target=on_closing)
#
# window.protocol("WM_DELETE_WINDOW", lambda: t.start())
#
# window.mainloop()
# ======================================================
# ======================================================

import customtkinter as ctk
import tkinter as tk
from Scanner import WebcamCapture

class RecogniPilajaraApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("1500x820")
        self.window.title("Recogni Pilajara")
        self.window.rowconfigure(0, weight=1)

        self.addButton = ctk.CTkButton(self.window, text="Add Data")
        self.addButton.grid(row=0, column=1, ipadx=10)

        self.Lframe_PgMain = ctk.CTkFrame(self.window, corner_radius=0, width=300)
        self.Lframe_PgMain.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.Lframe_PgMain.grid_rowconfigure(10, weight=1)

        self.mainLabel = ctk.CTkLabel(self.Lframe_PgMain, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.scanButton = ctk.CTkButton(self.Lframe_PgMain, text="Scan")
        self.scanButton.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.Lframe_PgMain, text="Main Page", )
        self.mainButton.grid(row=8, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.Lframe_PgMain, text='Mode', variable=self.switchVari, onvalue=True, offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

        self.camlabel = tk.Label(self.window)
        self.camlabel.grid(row=0, column=2, padx=25, pady=(20, 0))

        self.webcam = WebcamCapture(self.camlabel)
        self.webcam.start()
        print("WEBCAM START")

        self.window.protocol("WM_DELETE_WINDOW", self.on_window_close)

        self.Rframe_pgmain = ctk.CTkFrame(self.window, corner_radius=0, width=600)
        self.Rframe_pgmain.grid(row=0, column=4, rowspan=4, sticky="nsew")
        self.Rframe_pgmain.grid_rowconfigure(10, weight=1)

        self.foto = tk.Canvas(self.Rframe_pgmain, height=200,width=200)
        self.foto.grid(row=0, column=0, padx=120, pady=20, sticky='w')
        self.foto.grid_propagate(0)

        self.nama = ctk.CTkLabel(master=self.Rframe_pgmain, text="MARIO",font=ctk.CTkFont(family='Davish', size=70, weight='bold'))
        self.nama.grid(row=1, column=0, padx=106, pady=10, sticky='w')

        self.sum_label = ctk.CTkLabel(master=self.Rframe_pgmain, text='16',font=ctk.CTkFont(family='Davish', size=200, weight='bold'))
        self.sum_label.grid(row=2, column=0, padx=100, pady=(10,12), sticky="w")

        self.button1 = ctk.CTkButton(master=self.Rframe_pgmain, text="Button 1")
        self.button1.grid(row=3, column=0, padx=20, pady=(10, 20), sticky='w')

        self.button2 = ctk.CTkButton(master=self.Rframe_pgmain, text="Button 2", )
        self.button2.grid(row=4, column=0, padx=20, pady=(10, 20), sticky='w')

        self.button3 = ctk.CTkButton(master=self.Rframe_pgmain, text="Button 3", )
        self.button3.grid(row=5, column=0, padx=20, pady=(10, 20), sticky='w')

    def on_window_close(self):
        self.webcam.stop()
        self.webcam.release()
        self.window.destroy()


        # Add event listeners
        # self.addButton.bind("<Button-1>", self.add_data)
        # self.scanButton.bind("<Button-1>", self.scan)
        # self.mainButton.bind("<Button-1>", self.main_page)
        # self.switch_1.bind("<Button-1>", self.toggle_mode)
        # self.button1.bind("<Button-1>", self.on_button1_click)
        # self.button2.bind("<Button-1>", self.on_button2_click)
        # self.button3.bind("<Button-1>", self.on_button3_click)

        # def add_data(self, event):
        #     # Functionality to add data
        #     pass
        #
        # def scan(self, event):
        #     # Functionality to scan
        #     pass
        #
        # def main_page(self, event):
        #     # Functionality to go back to main page
        #     pass
        #
        # def toggle_mode(self, event):
        #     # Functionality to toggle mode
        #     pass
        #
        # def on_button1_click(self, event):
        #     # Functionality for Button 1
        #     pass
        #
        # def on_button2_click(self, event):
        #     # Functionality for Button 2
        #     pass
        #
        # def on_button3_click(self, event):
        #     # Functionality for Button 3
        #     pass

app = RecogniPilajaraApp()

app.window.mainloop()
