#Importing Tkinter

from tkinter import *
from tkinter.ttk import *

#Importing Time

from time import strftime

#Root

root = Tk()
root.title("Clock")

#Making the set up of the clock 
def time():
    string = strftime("%Y-%m-%d  %H:%M:%S")
    Label.config(text=string)
    Label.after(1,time)

#Labels of the design
Label = Label(root, font=("", 50), background = "khaki", foreground = "red")
Label.pack(anchor="center")

time()

mainloop()

