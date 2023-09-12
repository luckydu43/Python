import math

from IMetaCalcGeo import IMetaCalcGeo

class Cercle(IMetaCalcGeo):
    def __init__(self, rayon):
        self.__rayon=rayon
    
    @property
    def rayon(self):
        return self.__rayon
    
    @property
    def surface(self):
        return math.pi*self.__rayon**2

    @rayon.setter
    def rayon(self, rayon):
        self.__rayon=rayon

    def __str__(self):
        return "Cercle de rayon " + str(self.__rayon)
    
    def __eq__(self, __value: object) -> bool:
        return __value.__rayon == self.__rayon