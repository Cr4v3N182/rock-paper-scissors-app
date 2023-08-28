from tkinter import *
import random

#main screen
master = Tk()
master.title("RPS")

#labels
Label(master,text="rock-paper-scissors", font=("Clibri", 14)).grid(row=0, sticky=N,
        pady=10, padx=200)
Label(master,text="Choose something", font=("Clibri", 14)).grid(row=0, sticky=N,
        pady=10, padx=200)

master.mainloop()
