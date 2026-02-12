# Auteur: Aurélien Nicollas
# Date: 12/02/2026
# Fonction: Afficher un écran de fin

# IMPORTS

import random
from time import sleep
from tkinter import *
from tkinter.font import *

# FENÊTRE

root = Tk()
root.geometry("600x600")
root.title("Jeu du 2048 - Menu")
font = Font(family="Century Gothic", size=70, weight=BOLD)
btn_font = Font(family="Century Gothic", size=50, weight=NORMAL)

# FONCTIONS

def play():
    root.destroy()
    import gfx

title = Label(root, text="Game over !", font=font, fg=("#ff5757"))
title.pack(pady=80)

btn_play = Button(root, text="Rejouer !", bg=("#8ad3f2"), fg="white", font=btn_font, width=14, command=play)
btn_play.pack(side=BOTTOM, pady=100)

# DÉMARRAGE

root.mainloop()