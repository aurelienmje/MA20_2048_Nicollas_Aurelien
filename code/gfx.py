# Auteur: Aurélien Nicollas
# Date: 12/02/2026
# Fonction: Afficher un 2048

# IMPORTS

import random
from time import sleep
from tkinter import *
from tkinter.font import *

# FENÊTRE

root = Tk()
root.geometry("600x600")
root.title("Jeu du 2048")
font = Font(family="Century Gothic", size=22, weight=BOLD)

# FONCTIONS

# Fontion qui sert à afficher les cases
def display():
    for line in range(4):
        for col in range(4):
            labels[line][col] = Label(frm_cases, text=cases[line][col], width=6, height=3, font=font, fg="white")
            print(cases[line][col])
            labels[line][col].grid(row=line, column=col, padx=5, pady=5)
            label_text = labels[line][col].cget("text")
            labels[line][col].config(bg=colors[label_text])

# CONSTANTES

colors = {
    "":"#f5f5f5",
    "2":"#9fc7aa",
    "4":"#d8d355",
    "8":"#ffc4d4",
    "16":"#c197d2",
    "32":"#cbb1b1",
    "64":"#a4d8c8",
    "128":"#f57e9a",
    "256":"#ff7d7d",
    "512":"#d8b4a4",
    "1024":"#f2e88a",
    "2048":"#977dff",
    "4096":"#7db1ff",
    "8192":"#97e59f"
}

# TABLEAUX

# Tableau des numéros de cases
cases = [["2", "4", "8", "16"],
         ["32", "64", "128", "256"],
         ["512", "1024", "2048", "4096"],
         ["8192", None, None, None]]

# Tableau des labels
labels = [[None,None,None,None],
          [None,None,None,None],
          [None,None,None,None],
          [None,None,None,None]]

# FRAME PRINCIPALE

frm_cases = Frame(root)
frm_cases.pack(pady=40)

# DÉMARRAGE

display()
root.mainloop()