from Home import Home
from AddData import AddData
import Const
import customtkinter as ctk

window = ctk.CTk()
window.geometry(Const.window_geo)
window.title("Recogni Pilajara")

home = Home(window)
home.getFrame()

# adddata = AddData(window)
# adddata.getFrame()

window.mainloop()