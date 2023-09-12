

from abc import ABCMeta, abstractmethod

"""
Ceci est une interface
"""
class IMetaCalcGeo(metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def surface(self):
        pass