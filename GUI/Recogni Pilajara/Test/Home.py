import Const
import cv2
import customtkinter as ctk
from PIL import ImageTk, Image

class Home:

    def __init__(self, window):
        # self.window = ctk.CTk()
        # self.window.geometry(Const.window_geo)
        # self.window.title("Recogni Pilajara")
        self.window = window

        self.frame = ctk.CTkFrame(self.window, width=Const.window_width, height=Const.window_height)
        self.frame.grid(row=1, column=1)

        self.Lframe_PgMain = ctk.CTkFrame(self.frame, corner_radius=0, width=300, height=Const.window_height, fg_color='black')
        self.Lframe_PgMain.grid(row=1, column=0)

        self.Cframe_PgMain = ctk.CTkFrame(self.frame, corner_radius=0, width=480, height=Const.window_height)
        self.Cframe_PgMain.grid(row=1, column=1)

        self.Rframe_PgMain = ctk.CTkLabel(self.frame, width=300, height=Const.window_height, fg_color='black', text=None)
        self.Rframe_PgMain.grid(row=1, column=2)

        self.mainLabel = ctk.CTkLabel(self.Lframe_PgMain, text="RecogniPilajara", font=ctk.CTkFont(family='Davish', size=20, weight='bold'))
        self.mainLabel.grid(row=1, column=1, padx=55, pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_PgMain, text="Home", height=30)
        self.addButton.grid(row=2, column=1, pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_PgMain, text="STOP", height=30, command=self.stop_video)
        self.addButton.grid(row=3, column=1, pady=(30, 10))

        self.addButton = ctk.CTkButton(self.Lframe_PgMain, text="SCAN", height=30, command=self.update_video)
        self.addButton.grid(row=4, column=1, pady=(30, 10))

        self.mainLabel = ctk.CTkLabel(self.Lframe_PgMain, text=None, height=443)
        self.mainLabel.grid(row=5, column=1)

        self.video_frame = ctk.CTkFrame(self.Cframe_PgMain, width=640, height=480)
        self.video_frame.pack()

        self.video_capture = cv2.VideoCapture(0)

        self.video_label = ctk.CTkLabel(self.video_frame, text=None)
        self.video_label.pack()


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

    def getFrame(self):
        return (
            self.frame,

        )