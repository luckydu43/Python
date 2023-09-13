# https://www.codingame.com/ide/puzzle/mime-type
# 10% donc FAILED
# 3/4 pass dans IDE

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mtEnListe = []
typesMimes = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mtEnListe.append(mt)
    typeMimeDecoupe = ''
    typeMimeDecoupe = (mt.split('/'))
    typeMimeDecoupe = typeMimeDecoupe[len(typeMimeDecoupe) -1].split('-')
    typeMimeDecoupe = typeMimeDecoupe[len(typeMimeDecoupe) -1].upper()
    if typeMimeDecoupe == 'PLAIN':
        typeMimeDecoupe = 'TXT'
    typesMimes.append(typeMimeDecoupe)
    print("typeMimeDecoupe[1] :", typeMimeDecoupe, file=sys.stderr, flush=True)
print("mtEnListe :", mtEnListe, file=sys.stderr, flush=True)
for i in range(q):
    fname = input()  # One file name per line.
    print("fname :", fname, file=sys.stderr, flush=True)
    retour = 'UNKNOWN'
    if "." in fname:
        decoupeFName = fname.split(".")
        typeMimeDuFichier = decoupeFName[len(decoupeFName) -1].upper()
        print("typeMimeDuFichier :", typeMimeDuFichier, file=sys.stderr, flush=True)
        if typeMimeDuFichier in typesMimes:
            retour = mtEnListe[typesMimes.index(typeMimeDuFichier)]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(retour)

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
