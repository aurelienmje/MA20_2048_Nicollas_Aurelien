# Auteur: Aurélien Nicollas
# Date: 26/02/2026
# Fonction: Faire les règles du jeu

def fusion(a, b, c, d):
    cpt = 0
    if 0 in (a, b, c):
        if c == 0:
            c, d = d, 0
            cpt += 1
        if b == 0:
            b, c, d = c, d, 0
            cpt += 1
        if a == 0:
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

    print(a, b, c, d, "Effectué en", cpt, "coups")
    return [a, b, c, d]


fusion(0,0,0,2)
fusion(0, 0, 2, 2)
fusion(2, 0, 2, 2)
fusion(2, 2, 2, 2)
fusion(2, 2, 4, 0)
