
class Rectangle():

    nombreInstances = 0 # Variable statique car non liée à self_

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle.nombreInstances +=1

    @property
    def longueur(self):
        return self.__longueur
    @property
    def largeur(self):
        return self.__largeur
    @property
    def surface(self):
        return self.__longueur*self.__largeur

    @staticmethod
    def get_nombre_instances():
        return Rectangle.nombreInstances
    
    @classmethod
    def build_from_str(cls, str:str):
        listeParametres = str.split(",")
        return cls(listeParametres[0], listeParametres[1])

    @longueur.setter
    def longueur(self, longueur):
        self.__longueur = longueur
    
    @largeur.setter
    def largeur(self, largeur):
        self.__largeur = largeur
    
    def __del__(self): 
        print("__del__ Rectangle")
        Rectangle.nombreInstances -=1
    
    def __str__(self):
        return "Rectangle de longueur " + str(self.__longueur) + " et de largeur " + str(self.__largeur)
    
    def __eq__(self, __value: object) -> bool:
        return __value.__longueur == self.__longueur and __value.__largeur == self.__largeur