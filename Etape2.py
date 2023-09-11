def sommeElementsListe(liste):
    somme = 0
    for element in liste :
        somme = somme + element
    return somme

"""
Prend en paramètre un ensemble variable d'élements en entrée
et en retourne la somme

Pour obtenir la somme des élements d'une liste, placer *liste
"""
def sommeElements(*elements):
    print ('parametres de sommeElements = ' + str(elements))
    somme = 0
    for element in elements :
        somme = somme + element
    return somme

def Etape2 ():
    liste=[10, 20, 30]
    #print('Somme d\' une liste : ' + str(sommeElementsListe(liste))) #60
    print('Somme d\' une liste : ' + str(sommeElements(*liste))) #60
    print('Somme d\'éléments : ' + str(sommeElements(10,20,30))) #60

if __name__ == "__main__":
    Etape2()