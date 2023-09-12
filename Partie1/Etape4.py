from math import sqrt


def Etape4():
    print(50*'-')
    print ("Algorithme affichant la liste des premiers")
    print ("nombres premiers inférieurs à 100")
    print(50*'-')
    for valeurAtester in range (2,100):
        for compteur in range (2,int(sqrt(valeurAtester)+1)):
            if valeurAtester % compteur ==0:
                break
        else:
            print(valeurAtester)
if __name__ == "__main__":
    Etape4()