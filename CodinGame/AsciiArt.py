# https://www.codingame.com/ide/puzzle/ascii-art
# Success

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

lignesASCII = []
for i in range(h):
    lignesASCII.append(input())

# On effectue le parcours ligne à ligne pour n'avoir que le nombre demandé de print
for ligneASCII in lignesASCII:
    # ligne a afficher dans chaque print
    ligneAffichee = ''

    """
    On parcours les caractères de t, le string a convertir
    Pour chaque caractere :
    - 1. On récupère sa valeur ASCII
    - 2. On déduit sa position dans l'ordre alphabétique
    - 3. connaissant la largeur d'un caractère ASCII on en déduit sa
        position dans la chaine ASCII en prenant en compte les espaces
    - 4. connaissant la hauteur d'un caractère ASCII on l'affiche
    """
    for caractere in t:
        # 1.
        valeurASCII = ord(caractere)

        # 2.
        """
        Il y a 2*26+1 valeurs possibles :
        - [A~Z] valant [65~90] ayant une position [1~26]
        - [a~z] valant [97~122] ayant une position [1~26]
        - tout le reste affiché par ? en position 27
        """
        # position par défaut
        position = 27
        # Si on est un [A~Z]
        if valeurASCII >= 65 and valeurASCII <=90:
            position = valeurASCII - 64
        # Si on est un [a~z]
        if valeurASCII >= 97 and valeurASCII <=122:
            position = valeurASCII - 96

        # 3.
        indexBoutDeString = position*(l)-l

        # 4.
        ligneAffichee = ligneAffichee + ligneASCII[indexBoutDeString : indexBoutDeString + l]

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(ligneAffichee)
