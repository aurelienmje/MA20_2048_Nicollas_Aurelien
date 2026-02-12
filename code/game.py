# Auteur: Aurélien Nicollas
# Date: 12/02/2026
# Fonction: Faire les règles du jeu

# IMPORTS

import random
from time import sleep
from tkinter import *

# FENÊTRE

root = Tk()
root.geometry("300x300")

# CONSTANTES

colors = {
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

cases = [1, 2, 2, 2]
print(cases)

def Up(key):
    global cases
    for i in range(3):
        if cases[i] == cases[i+1]:
            cases[i+1] = cases[i+1] + cases[i]
            cases[i] = 0
    for i in range(3):
        if cases[i] != 0 and cases[i + 1] == 0:
            cases[i + 1] = cases[i]
            cases[i] = 0
    """cases[3] = cases[3] + cases[2]
    cases[2] = 0
    cases[1] = cases[1] + cases[0]
    cases[0] = 0
    for i in range(3):
        if cases[i] != 0 and cases[i+1] == 0:
            cases[i+1] = cases[i]
            cases[i] = 0"""
    print(cases)

# BOUCLE RUNNING

root.bind('<space>', Up)
root.mainloop()