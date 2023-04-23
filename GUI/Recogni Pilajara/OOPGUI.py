import customtkinter as ctk
import tkinter as tk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.window = ctk.CTk()

    def mainWindow(self):
        self.window.geometry("1500x820")
        self.window.title("Recogni Pilajara")
        self.window.rowconfigure(0, weight=1)

        self.leftFrame()
        self.centerFrame()
        self.rightFrame()

        self.window.mainloop()
    def leftFrame(self):
        self.Lframe_pgmain = ctk.CTkFrame(self.window, corner_radius=0, width=300)
        self.Lframe_pgmain.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.Lframe_pgmain.grid_rowconfigure(10, weight=1)

        self.mainLabel = ctk.CTkLabel(self.Lframe_pgmain, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.Addbutton = ctk.CTkButton(self.Lframe_pgmain, text="Main Page")
        self.Addbutton.grid(row=5, column=1, padx=55, pady=(30, 10))

        self.scanButton = ctk.CTkButton(self.Lframe_pgmain, text="Add Data")
        self.scanButton.grid(row=6, column=1, padx=55, pady=(30, 10))

        self.mainButton = ctk.CTkButton(self.Lframe_pgmain, text="Scan", fg_color='red')
        self.mainButton.grid(row=7, column=1, padx=55, pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.Lframe_pgmain, text='Mode', variable=self.switchVari, onvalue=True, offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

    def centerFrame(self):
        self.video = ctk.CTkButton(self.window, width=640, height=480)
        self.video.grid(row=0, column=2, rowspan=4, sticky="w", padx=85)

    def rightFrame(self):
        self.Rframe_pgmain = ctk.CTkFrame(self.window, corner_radius=0, width=500)
        self.Rframe_pgmain.grid(row=0, column=4, rowspan=4, sticky="nsew")
        self.Rframe_pgmain.grid_rowconfigure(10, weight=1)

        self.foto = tk.Canvas(self.Rframe_pgmain, height=200,width=200)
        self.foto.grid(row=0, column=0, padx=120, pady=20, sticky='w')
        self.foto.grid_propagate(0)

        self.nama = ctk.CTkLabel(master=self.Rframe_pgmain, text="MARIO",font=ctk.CTkFont(family='Davish', size=70, weight='bold'))
        self.nama.grid(row=1, column=0, padx=106, pady=10, sticky='w')

        self.sum_label = ctk.CTkLabel(master=self.Rframe_pgmain, text='16',font=ctk.CTkFont(family='Davish', size=200, weight='bold'))
        self.sum_label.grid(row=2, column=0, padx=100, pady=(10,12), sticky='w')

        self.mainButton = ctk.CTkButton(master=self.Rframe_pgmain, text='KEHADIRAN', font=ctk.CTkFont(family='Davish', size=30, weight='bold'),hover=False)
        self.mainButton.grid(row=10, column=0, padx=125, pady=1, sticky='w')


app = App()
app.mainWindow()