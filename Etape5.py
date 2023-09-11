def fonction_compteur_cache(compteur):
    print (f"create make_incrementor {compteur=}")
    def sous_fonction_compteur(increment):
         return compteur + increment
    return sous_fonction_compteur

def Etape5():
    print(50*'-')
    print ("Closures")
    print(50*'-')
    compteur1 = fonction_compteur_cache(10)
    compteur2 = fonction_compteur_cache(20)
    v1 = compteur1(1)
    v2 = compteur2(10)
    print (v1)
    print (v2)
    print ("Appel d'une fonction et de sa sous-fonction")
    print(fonction_compteur_cache(20)(10))

if __name__ == "__main__":
    Etape5()