import tkinter  as tk

from tkinter import ttk
# importing strftime function to
# retrieve system's time
from time import strftime


# creating tkinter window
root = tk.Tk()

root.title('Clock')


# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p \n %x')

    lbl.config(text=string)
    lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = tk.Label(root, font=('calibri', 40, 'bold'),
               background='purple',
               foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

tk.mainloop()