from DataRectangle import DataRectangle
from Rectangle import Rectangle

def Etape8():
    print(50*'-')
    print ("Classe, accesseurs, entite")
    print(50*'-')

    r = Rectangle(3,2)
    datarectangle = DataRectangle(12,3,3*12)
    print("datarectangle longueur", datarectangle.longueur)
    print("datarectangle largeur", datarectangle.largeur)
    print("datarectangle surface", datarectangle.surface)
    print(r.longueur) #3
    print(r.largeur) #2
    print(r.surface) #6
    
    print(50*'-')
    print("ToString")
    print("largeur :", r.largeur)
    print(r)
    print(50*'-')

    print("equals")
    r1 = Rectangle(3,2)
    print("Normalement c'est vrai :", r1==r)
    print(50*'-')

    print("Usage setter")
    r.longueur = 12
    print("surface :", r.surface)

    print(50*'-')
    print("Fin de classe")
if __name__ == "__main__":
    Etape8()