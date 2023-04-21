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
                self.label.config(image=imgtk)
                self.label.image = imgtk

def main():
    # Create customtkinter window
    root = tk.CustomTkinter()
    root.title("Webcam Display")

    # Create label to display webcam feed
    label = tk.Label(root)
    label.pack()

    # Create webcam capture object
    webcam = WebcamCapture(label)
    webcam.start()

    root.mainloop()

if __name__ == "__main__":
    main()
