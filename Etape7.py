def division(a,b):
    return a/b

def appel_division(a,b):
    try:
        print("avant")
        resultat = division(a,b)
    finally:
        print ("apres")
    return resultat

def isNombreNonNul(b):
    resultat = False
    if b.isdigit():
        if b!=0:
            resultat = True
    return resultat

def Etape7():
    print(50*'-')
    print ("Gestion des exceptions + Do / While")
    print(50*'-')
    try:
        a = 2
        """
        Structure Do / While
        """
        while True:
            b = input("Valeur b = ")
            if isNombreNonNul(b):
                b = int(b)
                break
        c = appel_division(a,b)
        print(a, "/", b, "=", c)
    except ZeroDivisionError as e:
        print("Erreur, b est égal à 0")
    except ValueError as e:
        print("Erreur, b n'est pas un nombre")
    except Exception as e:
        print("Exception", e)
    else:
        print("Aucune erreur rencontrée")

if __name__ == "__main__":
    Etape7()