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
            b = int(input("Valeur b = "))
            if b!=0 :
                break
        c = a / b
        print(c)
    except ZeroDivisionError as e:
        print("Erreur, b est égal à 0")
    except ValueError as e:
        print("Erreur, b n'est pas un nombre")
    except Exception as e:
        print("Exception", e)
    print(a)

if __name__ == "__main__":
    Etape7()