from IMetaCalcGeo import IMetaCalcGeo


class Rectangle(IMetaCalcGeo):
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    @property
    def longueur(self):
        return self.__longueur
    @property
    def largeur(self):
        return self.__largeur
    @property
    def surface(self):
        return self.__longueur*self.__largeur

    @longueur.setter
    def longueur(self, longueur):
        self.__longueur = longueur
    
    @largeur.setter
    def largeur(self, largeur):
        self.__largeur = largeur

    def __del__(self): 
        print("__del__ Rectangle")
    
    def __str__(self):
        return "Rectangle de longueur " + str(self.__longueur) + " et de largeur " + str(self.__largeur)
    
    def __eq__(self, __value: object) -> bool:
        return __value.__longueur == self.__longueur and __value.__largeur == self.__largeur