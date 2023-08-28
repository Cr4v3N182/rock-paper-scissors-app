from tkinter import *
import random

#main screen
master = Tk()
master.title("RPS")

#labels
Label(master,text="rock-paper-scissors", font=("Clibri", 14)).grid(row=0, sticky=N,
        pady=10, padx=200)
Label(master,text="Choose something", font=("Clibri", 12)).grid(row=1, sticky=N)
player_score_label = Label(master,text="Player : 0", font=("Clibri", 12))
player_score_label.grid(row=2, sticky=W)
computer_score_label = Label(master,text="Computer : 0", font=("Clibri", 12))
computer_score_label.grid(row=2, sticky=E)
player_choice_label = Label(master,font=("Calibri", 12))
player_choice_label.grid(row=3, sticky=W)
computer_choice_label = Label(master,font=("Calibri", 12))
computer_choice_label.grid(row=3, sticky=E)
outcome_label = Label(master,font=("Calibri", 12))
outcome_label.grid(row=3, sticky=N)

#Buttons
Button(master, text="Rock", width=15,
       command=lambda:outcome_handler("rock")).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text="Paper", width=15,
       command=lambda:outcome_handler("paper")).grid(row=4, sticky=N, pady=5)
Button(master, text="Scissors", width=15,
       command=lambda:outcome_handler("scissors")).grid(row=4, sticky=E, padx=5, pady=5)

master.mainloop()
