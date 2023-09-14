from typing import Any


class TheClass:

    # Méthode existante par défaut mais qu'on n'implemente jamais
    def __new__(cls):
        print("on entre dans le new")
        # façon de créer une instance de TheClass puis lui appeler init pour la construire
        return super(TheClass, cls).__new__(cls)

    def __init__(self) -> None:
        print("on entre dans l'init")
    
    # ceci rend la classe TheClass callable
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("on entre dans le call")

def main():
    print(50*'-')
    print ("Cours gestion des instances")
    print(50*'-')
          
    instance = TheClass()
    instance()

if __name__=='__main__':
    main()