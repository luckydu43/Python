


from collections import deque


def Etape3():
    print(50*'-')
    print ("Operations sur ensembles de données")
    print(50*'-')
    liste1 = [10, 20, 30]
    print ("Liste initiale")
    print(liste1)
    print ("On ajoute une valeur au début")
    liste1.insert(0,1)
    print(liste1)
    print ("On pop la derniere valeur")
    derniereValeur = liste1.pop()
    print (derniereValeur)
    print ("La liste a été impactée")
    print(liste1)
    print(50*'-')
    print ("Operations sur collection deque")
    print(50*'-')
    deque1 = deque(liste1)
    print ("Deque initiale")
    print (deque1)
    print ("On ajoute une valeur au début")
    deque1.appendleft(0)
    print(deque1)
    print ("On pop la derniere valeur")
    derniereValeur = deque1.pop()
    print (derniereValeur)
    print ("La Deque a été impactée")
    print(deque1)
if __name__ == "__main__":
    Etape3()