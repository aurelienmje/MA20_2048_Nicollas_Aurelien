# Auteur: Aurélien Nicollas
# Date: 26/02/2026
# Fonction: Faire les règles du jeu
from idlelib.autocomplete_w import KEYPRESS_VIRTUAL_EVENT_NAME
#IMPORTS

import os
import gfx
import random
from tkinter.messagebox import *
from tkinter import *

score = 0

# FONCTIONS

def menu():
    menu = Tk()
    menu.geometry("200x200")
    menu.title("Menu")

    import_btn = Button(menu, text="Importer", command=import_game)
    import_btn.pack(pady=30)

    save_btn = Button(menu, text="Sauvegarder", command=save_game)
    save_btn.pack(pady=30)

def import_game():
    import json
    global score
    try:
        with open("./code/game.json", "r") as game_saved:
            data = json.load(game_saved)
            for line in range(4):
                for col in range(4):
                    cases[line][col] = data["cases"][line][col]
            score = data["score"]
            gfx.display()
        showinfo(title="Info", message="Votre jeu a été correctement chargé !")
    except:
        showinfo(title="Info", message="Une erreur est survenue")

def save_game():
    import json
    try:
        with open("./code/game.json", "w") as game_file:
            game = {"cases": cases, "score": score}
            json.dump(game, game_file, indent=2)
            showinfo(title="Info", message="Votre jeu a été sauvegardé !")
    except:
        showinfo(title="Info", message="Une erreur est survenue")

def Isgameover():
    cpt_possibles_moves = 0
    for line in range(4):
        for col in range(3):
            try:
                if cases[line][col] == cases[line][col+1]:
                    cpt_possibles_moves += 1
            except IndexError:
                continue
            try:
                if cases[line][col] == cases[line+1][col]:
                    cpt_possibles_moves += 1
            except IndexError:
                continue
    for line in range(4):
        for col in range(4):
            if cases[line][col] == 0:
                cpt_possibles_moves += 1
    if not cpt_possibles_moves > 0:
        gfx.display()
        print(cpt_possibles_moves)
        showinfo(title="Game Over !", message="Le jeu est fini !")

# Cette fonction sert à fusionner les cases
def pack4(a, b, c, d):
    score = 0
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
        score += a
    if b == c and b > 0:
        b, c, d = b * 2, d, 0
        cpt += 1
        score += b
    if c == d and c > 0:
        c, d = c * 2, 0
        cpt += 1
        score += c
    return [a, b, c, d, cpt, score]

# Cette fonction sert à faire apparaître des blocs dans une case vide aléatoire à chaque mouvement
def RandomAppear():
    empty_list = []
    for line in range(4):
        for col in range(4):
            if cases[line][col] == 0:
                empty_list.append((line, col))
    target_case = random.choice(empty_list)
    number = random.choice([2, 2, 2, 2, 4])
    gfx.cases[target_case[0]][target_case[1]] = number

# Cette fonction sert à détecter si un 2048 se trouve dans le tableau des cases
done = False
def Isthere2048():
    global done
    for line in range(4):
        for col in range(4):
            if cases[line][col] == 2048 and done == False:
                gfx.display()
                showinfo(title="Vous avez gagné !", message="Bravo, vous avez gagné !")
                done = True

# Cette fonction sert juste à ne pas répéter certaines instructions communes à toutes les fonctions suivantes
def key_pressed_actions(cpt_tot, score_tot, event):
    global score
    print()
    print("Effectué en", cpt_tot, "coups")
    if cpt_tot > 0:
        print("Des coups ont étés effectués", "Et vous avez pressé la touche : " + event.keysym)
        RandomAppear()
        Isthere2048()
        Isgameover()
    else:
        print("Aucun coup n'a été effectué")
    score += score_tot
    print(score)
    gfx.display()

# Cette fonction sert à détecter si la touche flèche du haut a été pressée
def Up(event):
    score_tot = 0
    score = 0
    get_cpt = 0
    cpt_tot = 0
    for col in range(4):
        cases[0][col], cases[1][col], cases[2][col], cases[3][col], get_cpt, score = pack4(cases[0][col], cases[1][col], cases[2][col], cases[3][col])
        cpt_tot = cpt_tot + get_cpt
        score_tot += score
    key_pressed_actions(cpt_tot, score_tot, event)

# Cette fonction sert à détecter si la touche flèche du bas a été pressée
def Down(event):
    score_tot = 0
    score = 0
    get_cpt = 0
    cpt_tot = 0
    for col in range(4):
        cases[3][col], cases[2][col], cases[1][col], cases[0][col], get_cpt, score = pack4(cases[3][col], cases[2][col], cases[1][col], cases[0][col])
        cpt_tot = cpt_tot + get_cpt
        score_tot += score
    key_pressed_actions(cpt_tot, score_tot, event)

# Cette fonction sert à détecter si la touche flèche de gauche a été pressée
def Left(event):
    score_tot = 0
    score = 0
    get_cpt = 0
    cpt_tot = 0
    for row in range(4):
        cases[row][0], cases[row][1], cases[row][2], cases[row][3], get_cpt, score = pack4(cases[row][0], cases[row][1], cases[row][2], cases[row][3])
        cpt_tot = cpt_tot + get_cpt
        score_tot += score
    key_pressed_actions(cpt_tot, score_tot, event)

# Cette fonction sert à détecter si la touche flèche de droite a été pressée
def Right(event):
    score_tot = 0
    score = 0
    get_cpt = 0
    cpt_tot = 0
    for row in range(4):
        cases[row][3], cases[row][2], cases[row][1], cases[row][0], get_cpt, score = pack4(cases[row][3], cases[row][2], cases[row][1], cases[row][0])
        cpt_tot = cpt_tot + get_cpt
        score_tot += score
    key_pressed_actions(cpt_tot, score_tot, event)

def restart():
    global score
    for line in range(4):
        for col in range(4):
            cases[line][col] = 0
    score = 0
    RandomAppear()
    RandomAppear()
    gfx.display()

# TABLEAUX

# Tableau des numéros de cases
cases = [[0, 0, 0, 0],
         [0, 2, 0, 0],
         [0, 0, 2, 0],
         [0, 0, 0, 0]]