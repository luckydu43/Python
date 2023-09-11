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

def bonjourToi(name, firstname):
    print ('Hello', firstname, name)

def bonjourVous(**kwargs):
    # Méthode 1
    for key in kwargs:
        print ('Hello', key, kwargs[key])
    # Méthode 2
    for key, value in kwargs.items():
        print ('Hello', value)

def testTuple():
    e=1
    f=2
    return e,f

def multipleListe(liste):
    listeMultipliee=[]
    for value in liste:
        listeMultipliee.append(value*2)
    return listeMultipliee

def mapperMultipleFois2(valeur):
    return valeur*2

def Etape2 ():
    print(50*'-')
    print ('Fonctions avec paramètres multiples')
    print(50*'-')
    liste=[10, 20, 30]
    #print('Somme d\' une liste : ' + str(sommeElementsListe(liste))) #60
    print('Somme d\' une liste : ' + str(sommeElements(*liste))) #60
    print('Somme d\'éléments : ' + str(sommeElements(10,20,30))) #60
    print(50*'-')
    print ('Fonctions avec paramètres par mots-clés')
    print(50*'-')
    bonjourToi(name="Dup", firstname="Luc")
    bonjourVous(firstname="Luc", name="Dup")
    print(50*'-')
    print ('Tuples')
    print(50*'-')
    a = (1,2)
    print(a)
    b = 1,2
    print(b)
    if a.__eq__(b):
        print ("Yes you")
    else:
        print ("Noo")
    c,d = 1,2
    print (c)
    print (d)
    if (b)==(testTuple):
        print ("Yes you")
    else:
        print ("Noo")
    print(50*'-')
    print ('Listes mappées')
    print(50*'-')
    listeAmultiplier = [10,20,30]
    listeMultipliee = multipleListe(listeAmultiplier)
    listeMultiplieeParMapper = list(map(mapperMultipleFois2, listeAmultiplier))
    listeMultiplieeParMapperLambda = list(map(lambda i:i*2, listeAmultiplier))
    listeMultiplieeParIntention = [i*2 for i in listeAmultiplier]
    listeANettoyer = ["         fgkdoo    ", "dfodn        ", "             fdgd"]
    ListeNettoyeeParIntention = [i.strip() for i in listeANettoyer]
    print ("Liste de base")
    print(listeAmultiplier)
    print ("Liste multipliée par for")
    print(listeMultipliee)
    print ("Liste multipliée par mapper")
    print(listeMultiplieeParMapper)
    print ("Liste multipliée par une lambda")
    print(listeMultiplieeParMapperLambda)
    print ("Liste multipliée par une intention")
    print(listeMultiplieeParIntention)
    print (" ")
    print ("Liste a nettoyer")
    print (listeANettoyer)
    print ("Liste nettoyee par intention")
    print (ListeNettoyeeParIntention)
if __name__ == "__main__":
    Etape2()