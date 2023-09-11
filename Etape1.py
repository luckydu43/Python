from pprint import pprint
import unmodule
from copy import copy, deepcopy

def Etape1():
    valeur = 10
    print(valeur)
    print('nom test : ' + __name__)
    unmodule.hello()
    a=1
    print('a = ' + str(a) + ', id = ' + str(hex(id(a))))
    a=23304689730942085
    print('a = ' + str(a) + ', id = ' + str(hex(id(a))))
    b=23304689730942085
    print('b = ' + str(b) + ', id = ' + str(hex(id(b))))
    c=23304689730942085
    print('c = ' + str(c) + ', id = ' + str(hex(id(c))))


    print(50*'-')
    print ('Passons aux listes')
    print(50*'-')
    l = [10,20,30]
    l1 = l
    l[0] = 1000
    print (l)
    print (l1)
    print ('... parce que mutable')
    print (' ')
    l = [10,20,30]
    #l1 = l.copy built-in method copy of list object
    lcopie1del= copy(l) #avec l'import from copy import copy
    l2et3 = l[2:4] # Importe le 3eme et le 4eme. Le premier item est inclus, le second est exclu
    lcopie2del = l[:]
    print ('On modifie la valeur 1 de l par 1000')
    l[0] = 1000
    print (l)
    print('id l = ' + str(hex(id(l))))
    print (lcopie1del)
    print ('id l1 = ' + str(hex(id(lcopie1del))))
    print (l2et3)
    print ('id l2et3 = ' + str(hex(id(l2et3))))
    print (lcopie2del)
    print ('id lcopie2del = ' + str(hex(id(lcopie2del))))

    print(50*'-')
    print ('Passons aux listes imbriquées')
    print(50*'-')
    listeimbriquee = [
        [10, 20],
        [30, 40],
        [50, 60]
    ]
    print ('copie profonde avant insertion de 5000')
    listeimbriquee2 = copy.deepcopy(listeimbriquee)
    listeimbriquee[2][0] = 5000
    pprint(listeimbriquee)
    pprint(listeimbriquee2)

if __name__ == "__main__":
    test()