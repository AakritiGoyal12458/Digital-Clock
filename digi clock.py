from tkinter import *
from tkinter.ttk import *
from time import strftime   #to retrieve system's time

root=Tk() # create a window with title bar and other decoration
root.title('clock') #it gives the title, if not written anything it will take 'tk' as the title

def time():    # to display time on label
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label=Label(root, font=("boulder",68), background="black", foreground="red")
label.pack(anchor="center")
time()
mainloop()