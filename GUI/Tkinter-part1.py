import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

font = 'Arial 24 bold'

# Main Window
window = tk.Tk()
window.title("Recogni")
window.geometry('720x440')


# Label
title_label = ttk.Label(master= window, text = 'Recogni Pilajara', font=font)
title_label.pack()

def convert():
    data = Entry_int.get()
    sqrt = data**2
    out_String.set(f'Convert {sqrt}')

# input field
input_frame = ttk.Frame(master=window)
Entry_int = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable=Entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert,)
entry.pack(side='left')
button.pack(side='right')
input_frame.pack(pady= 10)

# output
out_String = tk.StringVar()
output_label = ttk.Label(master=window,
                         text="Output",
                         font=font,
                         textvariable=out_String)
output_label.pack()


# run
window.mainloop()