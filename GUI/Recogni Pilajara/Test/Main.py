from Home import Home
import Const
import cv2
import customtkinter as ctk
from PIL import ImageTk, Image

window = ctk.CTk()
window.geometry(Const.window_geo)
window.title("Recogni Pilajara")

home = Home(window)
home.getFrame()

window.mainloop()