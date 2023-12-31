def do_log(prefix=""):
    print(50*'-')
    print ("DECORATEURS")
    print ("On entre dans la fonction qui va injecter du code")
    def wrapper_f(func):
        print(50*'-')
        print ("On entre dans le premier wrapper")
        print ("log:",func) # S'il n'y a pas quelque chose en paramètre ça pète.
        def wrapper(*args, **kwargs):
            # pass
            print(50*'-')
            print("... on rentre dans le second wrapper")
            print ("On part de :", prefix, args, kwargs)
            r = func(*args, **kwargs)
            print ("On obtient :", r)
            print(50*'-')
            return r
        return wrapper
    return wrapper_f

@do_log('Logger')
def dis_bonjour(name):
    print(50*'-')
    print ("... on entre dans dis_bonjour")
    return f"Bonjour {name}"

def Etape6():
    print(50*'-')
    print ("... on entre dans etape6")
    prenom="Luc"
    print ("On appelle la fonction dis_bonjour qui réclame du code injecté")
    print ("JUST BEFORE PRINT")
    print(dis_bonjour(prenom))
    print ("JUST AFTER PRINT")

if __name__ == "__main__":
    Etape6()