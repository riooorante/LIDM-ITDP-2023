import cv2
import customtkinter as tk
from PIL import Image, ImageTk
import threading

class WebcamCapture:
    def __init__(self, label):
        self.label = label
        self.cap = cv2.VideoCapture(0)
        self.thread = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.thread = threading.Thread(target=self._update)
        self.thread.start()

    def stop(self):
        self.is_running = False
        self.thread.join()

    def _update(self):
        while self.is_running:
            ret, frame = self.cap.read()
            if ret:
                # Resize frame to fit in the label
                frame = cv2.resize(frame, (640, 480))
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(rgb_frame)
                imgtk = ImageTk.PhotoImage(image)
                self.label.configure(image=imgtk)
                self.label.image = imgtk

    def release(self):
        self.cap.release()
