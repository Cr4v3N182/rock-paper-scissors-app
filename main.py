import PySimpleGUI as sg
import random

sg.theme("DarkAmber")

score = []
cpu_options = ["rock", "paper", "scissors"]

def cpu_choice():
    cpu_item = random.choice(cpu_options)
    return cpu_item

label = sg.Text("Choose stone, paper or scissors, and try to gues what's in a box")
rock_button = sg.Button("Rock", key="rock")
paper_button = sg.Button("Paper", key="paper")
scissors_button = sg.Button("Scissors", key="scissors")
show_score_button = sg.Button("Show score", key="score")
exit_button = sg.Button("Exit", key="exit")
result = sg.Text("", key="output")
check_win_lose = sg.Text("", key="check")

layout = [[label], [[stone_button, paper_button, scissors_button]],
          [show_score_button, result], [exit_button]]

window = sg.Window("Stone-Paper-Scissor-APP", layout=layout, size= (400, 200),
                   element_justification='c')




window.close()

