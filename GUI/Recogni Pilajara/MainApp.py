import customtkinter as ctk
import tkinter as tk
# import firebase_admin
# import os
# import shutil
import cv2
from PIL import Image, ImageTk
from customtkinter import filedialog
# from firebase_admin import credentials
# from firebase_admin import db

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1500x820")
        self.title("Recogni Pilajara")

        self.container_mainPage = ctk.CTkFrame(self)
        self.container_addPage = ctk.CTkFrame(self)


        # Main Page LFramePg_Main
        self.Lframe_pgmain = ctk.CTkFrame(self.container_mainPage, corner_radius=0, width=300)
        self.Lframe_pgmain.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.Lframe_pgmain.grid_rowconfigure(10, weight=1)

        self.mainLabel = ctk.CTkLabel(self.Lframe_pgmain, text="RecogniPilajara",
                                      font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.Addbutton = ctk.CTkButton(self.Lframe_pgmain, text="Main Page", fg_color='red')
        self.Addbutton.grid(row=2, column=1, padx=55, pady=(30, 10))

        self.scanButton = ctk.CTkButton(self.Lframe_pgmain, text="Add Data", command=self.show_addPage)
        self.scanButton.grid(row=3, column=1, padx=55, pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_pgmain, text="SCAN", height=30, width=60,command=self.update_video)
        self.addButton.grid(row=4, column=1, padx=(0, 70), pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_pgmain, text="STOP", height=30, width=60, command=self.stop_video)
        self.addButton.grid(row=4, column=1, padx=(70, 0), pady=(30, 10))

        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.Lframe_pgmain, text='Mode', variable=self.switchVari, onvalue=True,
                                      offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

        # Center Video Sementara
        self.video = ctk.CTkButton(self.container_mainPage, width=640, height=480)
        self.video.grid(row=0, column=1, rowspan=4, sticky="w", padx=85)

        # Video Capture
        # self.mainLabel = ctk.CTkLabel(self.Lframe_pgmain, text=None, height=443)
        # self.mainLabel.grid(row=5, column=1)

        self.video_frame = ctk.CTkFrame(self.container_mainPage, width=640, height=480)
        self.video_frame.grid(row=0, column=1, rowspan=4, sticky="w", padx=85)

        self.video_capture = cv2.VideoCapture(0)

        # self.video_place = ctk.CTkLabel(self.video_frame, width=640, height=1, text=None)
        # self.video.grid(row=0, column=1, rowspan=4, sticky="w", padx=85)

        self.video_label = ctk.CTkLabel(self.video_frame, text=None)
        self.video_label.grid(row=0, column=1, rowspan=4, sticky="w", padx=0)

        # Rframe RFrame_PgMain
        self.Rframe_pgmain = ctk.CTkFrame(self.container_mainPage, corner_radius=0, width=500)
        self.Rframe_pgmain.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.Rframe_pgmain.grid_rowconfigure(10, weight=1)

        self.foto = tk.Canvas(self.Rframe_pgmain, height=200, width=200)
        self.foto.grid(row=0, column=0, padx=120, pady=20, sticky='w')
        self.foto.grid_propagate(0)

        self.nama = ctk.CTkLabel(master=self.Rframe_pgmain, text="MARIO",
                                 font=ctk.CTkFont(family='Davish', size=70, weight='bold'))
        self.nama.grid(row=1, column=0, padx=106, pady=10, sticky='w')

        self.sum_label = ctk.CTkLabel(master=self.Rframe_pgmain, text='16',
                                      font=ctk.CTkFont(family='Davish', size=200, weight='bold'))
        self.sum_label.grid(row=2, column=0, padx=100, pady=(10, 12), sticky='w')

        self.mainButton = ctk.CTkButton(master=self.Rframe_pgmain, text='KEHADIRAN',
                                        font=ctk.CTkFont(family='Davish', size=30, weight='bold'), hover=False)
        self.mainButton.grid(row=10, column=0, padx=125, pady=1, sticky='w')

        # second Frame Lframe_pgform
        self.leftFrame_pgform = ctk.CTkFrame(self.container_addPage, corner_radius=0, width=300)
        self.leftFrame_pgform.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.leftFrame_pgform.grid_rowconfigure(10, weight=1)

        self.Maintext = ctk.CTkLabel(self.leftFrame_pgform, text="RecogniPilajara",
                                     font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.Maintext.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.button1 = ctk.CTkButton(self.leftFrame_pgform, text="Main Page", command=self.show_main, )
        self.button1.grid(row=5, column=1, padx=55, pady=(30, 10))
        self.button1.bind('<Button-1>')

        self.button2 = ctk.CTkButton(self.leftFrame_pgform, text="Add Data", fg_color='red')
        self.button2.grid(row=6, column=1, padx=55, pady=(30, 10))


        self.switchVari = ctk.BooleanVar(value=True)
        self.switch_1 = ctk.CTkSwitch(self.leftFrame_pgform, text='Mode', variable=self.switchVari, onvalue=True,
                                      offvalue=False)
        self.switch_1.grid(row=13, column=1, padx=55, pady=(30, 10))

        # Frame Frame Form
        self.img = ctk.CTkImage(dark_image=Image.open('Resources/FormPhoto.png'))
        self.buttonpict = ctk.CTkButton(self.container_addPage, text='FOTO', height=300, width=300, corner_radius=20,
                                        image=self.img)
        self.buttonpict.grid(row=0, column=1, padx=110, pady=(1, 0))

        self.frameform = ctk.CTkFrame(self.container_addPage, width=470, height=1080, corner_radius=0,
                                      fg_color='black')
        self.frameform.grid(row=0, column=2, rowspan=1, padx=0)

        self.form = ctk.CTkFrame(self.frameform, width=340, height=460, corner_radius=20)
        self.form.grid(row=2, column=1, rowspan=1, padx=80, pady=130, sticky="ns")
        self.form.grid_rowconfigure(10, weight=1)
        self.form.grid_propagate(0)

        self.nameLabel = ctk.CTkLabel(self.form, text="Nama")
        self.nameLabel.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nameEntry = ctk.CTkEntry(self.form, placeholder_text="Nama", width=300)
        self.nameEntry.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimLabel = ctk.CTkLabel(self.form, text="NIM")
        self.nimLabel.grid(row=4, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.nimEntry = ctk.CTkEntry(self.form, placeholder_text="NIM", width=300)
        self.nimEntry.grid(row=5, column=1, columnspan=2, padx=20, pady=10, sticky="w")

        self.genderVar = ctk.StringVar(value="Prefer\not to say")
        self.genderLabel = ctk.CTkLabel(self.form, text="Jenis Kelamin")
        self.genderLabel.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        self.maleRadioButton = ctk.CTkRadioButton(self.form, text="Laki-Laki", variable=self.genderVar, value="He is")
        self.maleRadioButton.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        self.femaleRadioButton = ctk.CTkRadioButton(self.form, text="Perempuan", variable=self.genderVar,
                                                    value="She is")
        self.femaleRadioButton.grid(row=7, column=2, padx=20, pady=10, sticky="w")

        self.occupationLabel = ctk.CTkLabel(self.form, text="Program Studi")
        self.occupationLabel.grid(row=8, column=1, padx=20, pady=10, sticky="w")

        self.occupationOptionMenu = ctk.CTkOptionMenu(self.form,
                                                      values=["Sistem Informasi", "Matematika", "Fisika", "Kimia",
                                                              "Biologi"])
        self.occupationOptionMenu.grid(row=8, column=2, padx=20, pady=10, columnspan=2, sticky="w")

        self.saveButton = ctk.CTkButton(self.form, height=50, width=180, corner_radius=10, text='SAVE',
                                        font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.saveButton.grid(row=10, columns=3, padx=10, pady=(20, 10))


        # Resposible UI
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.container_mainPage.rowconfigure(0, weight=1)
        self.container_mainPage.columnconfigure(0, weight=1)
        self.container_mainPage.columnconfigure(1, weight=1)
        self.container_addPage.rowconfigure(0, weight=1)
        self.container_addPage.columnconfigure(0, weight=1)

        # Display Main Page
        self.show_main()


    def show_main(self):
        self.container_mainPage.grid(row=0, columns=1, sticky='nsew')
        self.container_addPage.grid_forget()

    def show_addPage(self):
        self.container_addPage.grid(row=0, columns=1, sticky='nsew')
        self.container_mainPage.grid_forget()

    # def Save_data(self):
    #     self.user_name = self.nameEntry.get()
    #     self.user_NIM = self.nimEntry.get()
    #     self.user_Gender = self.genderVar.get()
    #     self.user_Major = self.majorVar.get()
    #
    #     self.cred = credentials.Certificate("path/to/serviceAccountKey.json")
    #     firebase_admin.initialize_app(self.cred, {
    #         'databaseURL': "https://pilajara-d8d3f-default-rtdb.firebaseio.com"
    #     } )
    #     self.ref = db.reference('/')
    #
    #     data = {
    #         'ID':self.user_NIM,
    #         'Major':self.user_Major,
    #         'Kehadiran':0,
    #         'LastScan':0,
    #         'Nama':self.user_name
    #     }
    #
    #     self.ref.push(data)
    # def openPhoto(self):
    #     self.sep = r"\""
    #
    #     self.file_path = filedialog.askopenfilename()
    #     self.new_file_path = list(map(str, self.file_path.split(self.sep)))
    #     self.new_file_path[-1] = self.user_NIM
    #
    #     self.new_file_path = os.rename(self.file_path, self.sep.join(self.new_file_path))
    #     self.destination = "D:\Programming\Project\LIDM-ITDP-2023\GUI\Recogni Pilajara\Profile"
    #     self.listOfdata = os.listdir(self.destination)
    #
    #     if self.user_NIM not in self.listOfdata:
    #         shutil.copy(self.new_file_path, self.destination)
    def update_video(self):

        # Membaca frame video dari webcam
        ret, frame = self.video_capture.read()

        if ret:
            # Mengubah format frame dari BGR ke RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Mengubah frame menjadi objek Image
            image = Image.fromarray(frame)

            # Mengubah objek Image menjadi objek PhotoImage untuk ditampilkan di label
            photo = ImageTk.PhotoImage(image)

            if not self.video_label.winfo_exists():
                self.video_frame = ctk.CTkFrame(self.container_mainPage, width=640, height=480)
                self.video_frame.grid(row=0, column=1, rowspan=4, sticky="w", padx=85)

                self.video_label = ctk.CTkLabel(self.video_frame, text=None)
                # self.video_label.pack()
                self.video_label.grid(row=0, column=1, rowspan=4, sticky="w", padx=0)

            # Mengubah isi dari label dengan objek PhotoImage terbaru
            self.video_label.configure(image=photo)
            self.video_label.image = photo

        if self.video_capture.isOpened():
            # Mengulangi update setiap 10 milidetik
            self.after(10, self.update_video)
        else:
            self.video_capture = cv2.VideoCapture(0)


    def stop_video(self):
        # Menghentikan video capture
        self.video_capture.release()

        # Menghilangkan label tempat tampilan video
        self.video_frame.destroy()

    def des(self):
        self.frame.grid_forget()

    def getFrame(self):
        return (
            self.frame,
        )

app = App()
app.mainloop()

