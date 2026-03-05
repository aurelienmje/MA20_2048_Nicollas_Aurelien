# Auteur: Aurélien Nicollas
# Date: 12/02/2026
# Fonction: Afficher un 2048

# IMPORTS

import random
from time import sleep
from tkinter import *
from tkinter.font import *
from tkinter.messagebox import *
from rules import *

# FENÊTRE

root = Tk()
root.geometry("600x600")
root.title("Jeu du 2048")
font = Font(family="Century Gothic", size=22, weight=BOLD)

# FONCTIONS

# Fonction qui sert à afficher les cases
def display():
    for line in range(4):
        for col in range(4):
            labels[line][col].config(text="")
            if not cases[line][col] == 0:
                labels[line][col].config(text=cases[line][col])
                label_text = labels[line][col].cget("text")
            else:
                label_text = 0
            labels[line][col].config(bg=colors[label_text])


def move(event):
    key_pressed(event)
    display()

# CONSTANTES

colors = {
    0:"#f5f5f5",
    2:"#9fc7aa",
    4:"#d8d355",
    8:"#ffc4d4",
    16:"#c197d2",
    32:"#cbb1b1",
    64:"#a4d8c8",
    128:"#f57e9a",
    256:"#ff7d7d",
    512:"#d8b4a4",
    1024:"#f2e88a",
    2048:"#977dff",
    4096:"#7db1ff",
    8192:"#97e59f"
}

# TABLEAUX

# Tableau des labels
labels = [[None,None,None,None],
          [None,None,None,None],
          [None,None,None,None],
          [None,None,None,None]]

# FRAME PRINCIPALE

frm_cases = Frame(root)
frm_cases.pack(pady=40)

# DÉMARRAGE

for line in range(4):
    for col in range(4):
        if not cases[line][col] == 0:
            labels[line][col] = Label(frm_cases, text=cases[line][col], width=6, height=3, font=font, fg="white")
            label_text = labels[line][col].cget("text")
        else:
            labels[line][col] = Label(frm_cases, width=6, height=3, font=font, fg="white")
            label_text = 0
        labels[line][col].grid(row=line, column=col, padx=5, pady=5)
        labels[line][col].config(bg=colors[label_text])

root.bind('<Key>', move)