import Const
import cv2
import customtkinter as ctk
from PIL import ImageTk, Image

class AddData:

    def __init__(self, window):
        self.window = window
        self.window.title("Recogni Pilajara | Add Data")

        self.frame = ctk.CTkFrame(self.window, width=Const.window_width, height=Const.window_height)
        self.frame.grid(row=1, column=1)

        self.Lframe_PgMain = ctk.CTkFrame(self.frame, corner_radius=0, width=300, height=Const.window_height, fg_color='black')
        self.Lframe_PgMain.grid(row=1, column=0)

        self.Cframe_PgMain = ctk.CTkFrame(self.frame, corner_radius=0, width=480, height=Const.window_height)
        self.Cframe_PgMain.grid(row=1, column=1)

        self.Rframe_PgMain = ctk.CTkFrame(self.frame, corner_radius=0, width=470, height=Const.window_height)
        self.Rframe_PgMain.grid(row=1, column=2)

        self.mainLabel = ctk.CTkLabel(self.Lframe_PgMain, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_PgMain, text="Home", height=30, command=self.des)
        self.addButton.grid(row=2, column=1, pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_PgMain, text="Add Data", height=30)
        self.addButton.grid(row=3, column=1, pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_PgMain, text="SCAN", height=30, width=60, command=self.update_video)
        self.addButton.grid(row=4, column=1, padx=(0, 70), pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_PgMain, text="STOP", height=30, width=60, command=self.stop_video)
        self.addButton.grid(row=4, column=1, padx=(70, 0), pady=(30, 10))

        self.mainLabel = ctk.CTkLabel(self.Lframe_PgMain, text=None, height=443)
        self.mainLabel.grid(row=5, column=1)

        self.video_frame = ctk.CTkFrame(self.Cframe_PgMain, width=640, height=480)
        self.video_frame.pack()

        self.video_capture = cv2.VideoCapture(0)

        self.video_place = ctk.CTkLabel(self.video_frame, width=640, height=1, text=None)
        self.video_place.pack()

        self.video_label = ctk.CTkLabel(self.video_frame, text=None)
        self.video_label.pack()

        self.frameform = ctk.CTkFrame(self.Rframe_PgMain, width=470, height=Const.window_height, corner_radius=0, fg_color='black')
        self.frameform.grid(row=0, column=1, rowspan=1, padx=0)

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
        self.saveButton.grid(row=10, columns=3, padx=10, pady=(20,10))

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
                self.video_frame = ctk.CTkFrame(self.Cframe_PgMain, width=640, height=480)
                self.video_frame.pack()

                self.video_label = ctk.CTkLabel(self.video_frame, text=None)
                self.video_label.pack()

            # Mengubah isi dari label dengan objek PhotoImage terbaru
            self.video_label.configure(image=photo)
            self.video_label.image = photo

        if self.video_capture.isOpened():
            # Mengulangi update setiap 10 milidetik
            self.window.after(10, self.update_video)
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