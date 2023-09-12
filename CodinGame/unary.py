# https://www.codingame.com/ide/puzzle/unary
# Success

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def conversionCaractereEnBinaire(caractere):
    valeurDecimale = ord(caractere)
    if valeurDecimale == 0:
        chaineBinaire = "0"
    else:
        chaineBinaire = ""
        while valeurDecimale != 0:
            chaineBinaire = "01"[valeurDecimale & 1] + chaineBinaire
            valeurDecimale = valeurDecimale >>1
    return chaineBinaire.zfill(7)

def ajouterZerosAAffichage(affichage, valeurBit, nbBits):
    #Si la chaine n'est déjà pas vide on peut ajouter un espace
    if affichage != '':
        affichage = affichage + ' '
    # On ajoute d'office un zero
    affichage = affichage + '0'
    # Si les bits sont des zeros on commence par 2 zeros
    if valeurBit == '0':
        affichage = affichage + '0'
    # On ajoute un espace
    affichage = affichage + ' '
    # On ajoute le nombre de zeros en fonction du nombre de bits
    for compteur in range(0,nbBits):
        affichage = affichage + '0'
    return affichage

message = input()

# Initialisation
affichage = ''
# Le premier caractère n'est pas pris en compte
valeurBitPrecedente = 'premierCaractère'
nbBitsInchanges = 0
for caractere in message:
    for bit in conversionCaractereEnBinaire(caractere):
        # Si le caractère a changé il faut afficher la chaine precedente
        if bit != valeurBitPrecedente != 'premierCaractère':
            affichage = ajouterZerosAAffichage(affichage, valeurBitPrecedente, nbBitsInchanges)
            nbBitsInchanges = 0
        valeurBitPrecedente = bit
        nbBitsInchanges +=1
# une fois fini il ne faut pas oublier les derniers caractères puisqu'on traite les précédents dans la boucle
affichage = ajouterZerosAAffichage(affichage, valeurBitPrecedente, nbBitsInchanges)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(affichage)
