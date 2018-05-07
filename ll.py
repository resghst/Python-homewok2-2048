import Tkinter as tk
from time import sleep

root = tk.Tk()
var = tk.StringVar()
var.set('hello')

l = tk.Label(root, textvariable = var)
l.pack()

for i in range(6):
    sleep(1) # Need this to slow the changes down
    var.set('goodbye' if i%2 else 'hello')
    root.update_idletasks()