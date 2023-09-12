from Carre import Carre
from Cercle import Cercle
from IMetaCalcGeo import IMetaCalcGeo

def show_surface(o:IMetaCalcGeo):
    print("Surface :",o.surface)

def Etape9():
    print(50*'-')
    print ("Heritage")
    print(50*'-')
    print("Carre")
    print(50*'-')
    c = Carre(3)

    print("ToString")
    print("largeur :", c.largeur)
    print(c)
    print(50*'-')

    print("equals")
    c2 = Carre(3)
    print("Normalement c'est vrai :", c==c2)
    print(50*'-')

    print("Modification des proprietes parentes")
    c.cote=4
    show_surface(c)

    print(50*'-')
    print("Cercle")
	
    cercle = Cercle(3)

    print(50*'-')
    print("ToString")
    show_surface(cercle)
    print(cercle)
    print(50*'-')

    print("equals")
    cercle2 = Cercle(3)
    print("Normalement c'est vrai :", cercle==cercle2)
    print(50*'-')

    print("Modification des proprietes")
    cercle.rayon=4
    show_surface(cercle)

if __name__ == "__main__":
    Etape9()