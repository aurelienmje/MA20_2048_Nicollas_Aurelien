# Auteur: Aurélien Nicollas
# Date: 26/02/2026
# Fonction: Faire les règles du jeu

#IMPORTS

from tkinter import *
import gfx
import random
from tkinter import *

# FONCTIONS

# Cette fonction sert à fusionner les cases
def pack4(a, b, c, d):
    cpt = 0
    if 0 in (a, b, c):
        if c == 0 and d > 0:
            c, d = d, 0
            cpt += 1
        if b == 0 and c > 0:
            b, c, d = c, d, 0
            cpt += 1
        if a == 0 and b > 0:
            a, b, c, d = b, c, d, 0
            cpt += 1
    if a == b and a > 0:
        a,b,c,d = a * 2, c, d, 0
        cpt += 1
    if b == c and b > 0:
        b, c, d = b * 2, d, 0
        cpt += 1
    if c == d and c > 0:
        c, d = c * 2, 0
        cpt += 1

    return [a, b, c, d, cpt]

# Cette fonction sert à faire apparaître des blocs dans une case vide aléatoire à chaque mouvement
def RandomAppear():
    empty_list = []
    for line in range(4):
        for col in range(4):
            if gfx.labels[line][col].cget("text") == "":
                empty_list.append((line, col))
    target_case = random.choice(empty_list)
    number = random.choice([2, 2, 2, 2, 4])
    gfx.cases[target_case[0]][target_case[1]] = number
    empty_list = []

# Cette fonction sert à détecter les touches pressées
def Up(event):
    get_cpt = 0
    cpt_tot = 0
    for col in range(4):
        cases[0][col], cases[1][col], cases[2][col], cases[3][col], get_cpt = pack4(cases[0][col], cases[1][col], cases[2][col], cases[3][col])
        cpt_tot = cpt_tot + get_cpt
    print()
    print("Effectué en", cpt_tot, "coups")
    if cpt_tot > 0:
        print("Des coups ont étés effectués", "Et vous avez pressé la touche : " + event.keysym)
        RandomAppear()
    else:
        print("Aucun coup n'a été effectué")
    gfx.display()

def Down(event):
    get_cpt = 0
    cpt_tot = 0
    for col in range(4):
        cases[3][col], cases[2][col], cases[1][col], cases[0][col], get_cpt = pack4(cases[3][col], cases[2][col], cases[1][col], cases[0][col])
        cpt_tot = cpt_tot + get_cpt
    print()
    print("Effectué en", cpt_tot, "coups")
    if cpt_tot > 0:
        print("Des coups ont étés effectués", "Et vous avez pressé la touche : " + event.keysym)
        RandomAppear()
    else:
        print("Aucun coup n'a été effectué")
    gfx.display()

def Left(event):
    get_cpt = 0
    cpt_tot = 0
    for row in range(4):
        cases[row][0], cases[row][1], cases[row][2], cases[row][3], get_cpt = pack4(cases[row][0], cases[row][1], cases[row][2], cases[row][3])
        cpt_tot = cpt_tot + get_cpt
    print()
    print("Effectué en", cpt_tot, "coups")
    if cpt_tot > 0:
        print("Des coups ont étés effectués", "Et vous avez pressé la touche : " + event.keysym)
        RandomAppear()
    else:
        print("Aucun coup n'a été effectué")
    gfx.display()

def Right(event):
    get_cpt = 0
    cpt_tot = 0
    for row in range(4):
        cases[row][3], cases[row][2], cases[row][1], cases[row][0], get_cpt = pack4(cases[row][3], cases[row][2], cases[row][1], cases[row][0])
        cpt_tot = cpt_tot + get_cpt
    print()
    print("Effectué en", cpt_tot, "coups")
    if cpt_tot > 0:
        print("Des coups ont étés effectués", "Et vous avez pressé la touche : " + event.keysym)
        RandomAppear()
    else:
        print("Aucun coup n'a été effectué")
    gfx.display()

# TABLEAUX

# Tableau des numéros de cases
cases = [[4, 0, 2, 2],
         [2, 2, 0, 0],
         [0, 2, 2, 4],
         [4, 4, 2, 4]]