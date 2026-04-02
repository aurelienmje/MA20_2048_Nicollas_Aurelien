# Auteur: Aurélien Nicollas
# Date: 12/02/2026
# Fonction: Afficher un 2048

# IMPORTS

from tkinter import *
from tkinter.font import *
from rules import *
import rules

# FENÊTRE

root = Tk()
root.geometry("600x650")
root.title("Jeu du 2048")
font = Font(family="Century Gothic", size=22, weight=BOLD)
font_score = Font(family="Century Gothic", size=12, weight=BOLD)

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
    score_text = f"Score : {rules.score}"
    score_lbl.config(text=score_text)
    print(rules.score)


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

# FRAME BOUTON MENU

menu = Button(root, text="Menu", command=menu)
menu.pack(anchor=E)

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

frm_btns = Frame(root, width=600, height=50)
frm_btns.pack()

btn_restart = Button(frm_btns, text="Recommencer", width=20, height=2, command=restart)
btn_restart.config(bg="white")
btn_restart.pack(side=LEFT, padx=70)

score_lbl = Label(frm_btns, text="Score : 0", font=font_score)
score_lbl.pack(side=RIGHT, padx=90)

root.bind('<Up>', Up)
root.bind('<Down>', Down)
root.bind('<Left>', Left)
root.bind('<Right>', Right)