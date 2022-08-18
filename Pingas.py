from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.geometry("750x250")

def close_win():
   root.destroy()
def disable_event():
   pass

root = Tk()
frm = ttk.Frame(root, padding=500)
frm.grid()
ttk.Label(frm, text="You got killed victoms PC").grid(column=0, row=0)
ttk.Button(frm, text="Haha LoL", command=root.quit).grid(column=8, row=40)
ttk.Button(frm, text="Hey Stinki", command=root.quit).grid(column=9, row=40)
ttk.Button(frm, text="hello yout cumpuper is a virus", command=root.quit).grid(column=10, row=10)
ttk.Button(frm, text="Bruh", command=root.quit).grid(column=7, row=7)
ttk.Button(frm, text="Haha Pingas", command=root.quit).grid(column=109, row=28)
ttk.Button(frm, text="Get out of my room im playing minecraft", command=root.quit).grid(column=78, row=60)
ttk.Button(frm, text="Ich hab in U-Bahn gekackt", command=root.quit).grid(column=94, row=44)
ttk.Button(frm, text="get free robux", command=root.quit).grid(column=15, row=10)
ttk.Button(frm, text="Im under the walter", command=root.quit).grid(column=72, row=55)
ttk.Button(frm, text="Hold up", command=root.quit).grid(column=101, row=59)
ttk.Button(frm, text="U suck", command=root.quit).grid(column=87, row=10)
ttk.Button(frm, text="Get wricked noob", command=root.quit).grid(column=98, row=4)
ttk.Button(frm, text="Happy piss day for yu", command=root.quit).grid(column=17, row=16)
ttk.Button(frm, text="Air up", command=root.quit).grid(column=73, row=71)
ttk.Button(frm, text="Give me money", command=root.quit).grid(column=30, row=39)
root.protocol("WM_DELETE_WINDOW", disable_event)
root.mainloop()
