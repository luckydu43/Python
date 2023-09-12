from Rectangle import Rectangle

class Carre(Rectangle):
    def __init__(self, cote):
        self.__cote=cote
        super().__init__(cote, cote)
    
    @property
    def cote(self):
        return self.__cote
    
    @cote.setter
    def cote(self, cote):
        self.__cote=cote
        self.longueur=cote
        self.largeur=cote

    def __str__(self):
        return "Carre de cote " + str(self.__cote)
    
    def __eq__(self, __value: object) -> bool:
        return __value.__cote == self.__cote