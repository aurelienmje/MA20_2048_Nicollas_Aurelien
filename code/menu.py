# Auteur: Aurélien Nicollas
# Date: 05/02/2026
# Fonction: Afficher un 2048

# IMPORTS

import random
from time import sleep
from tkinter import *
from tkinter.font import *

# FENÊTRE

root = Tk()
root.geometry("600x600")
font = Font(family="Century Gothic", size=100, weight=BOLD)
btn_font = Font(family="Century Gothic", size=50, weight=NORMAL)

# FONCTIONS

def play():
    root.destroy()
    import gfx

title = Label(root, text="2048", font=font)
title.pack(pady=40)

btn_play = Button(root, text="Jouer !", bg=("#8ad3f2"), fg="white", font=btn_font, width=14, command=play)
btn_play.pack(side=BOTTOM, pady=100)

# DÉMARRAGE

root.mainloop()