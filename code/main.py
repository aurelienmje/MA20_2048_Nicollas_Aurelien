# Auteur: Aurélien Nicollas
# Date: 12/02/2026
# Fonction: Compiler tout les programmes

# CECI EST TEMPORAIRE
# CE CODE SERT UNIQUEMENT À LA VÉRIFICATION DE MON TRAVAIL

print("""Que souhaitez-vous voir ? :
[1] Menu
[2] Gameover""")
temp = input("1 ou 2 : ")
if temp == "1":
    import menu
else:
    import game_over