
import tkinter as tk
from tkinter import ttk


def button():
    print("Button was Press")

def button2():
    print("hello")

# buat window
window = tk.Tk()
window.title("APP")
window.geometry("1400x720")

# ttk Widgets
label = ttk.Label(master=window, text="Ini Adalah Text")
label.pack()

# WIdgets
text = tk.Text(master=window)
text.pack()

# Entry
entry = ttk.Entry(master=window)
entry.pack()

# Latihan
frameLatihan = ttk.Frame(master=window)
label2 = ttk.Label(master=frameLatihan, text="My label")
button2 = ttk.Button(master=frameLatihan, text="Klik", command=button2())
label2.pack(side='left')
button2.pack(side='left')
frameLatihan.pack()

# Button
button = ttk.Button(master=window, text="Tekan", command=button())
button.pack()




#run
window.mainloop()
