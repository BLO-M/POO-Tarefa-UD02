from abc import ABC, abstractmethod
from .common import *

class Dispositivo(ABC):
    def __init__(self, _id : str, _nombre : str, _fabricante : str):
        #Implemento directamente validar y no fabricar porque ya parto del atributo id, no tengo prefijo ni número
        #Tampoco tengo clara la validación que se solicita, lo único el tipo por lo que hago isinstance y genero error personalizado
        if Utils.validar_id(_id):
            self._id = _id
        else:
            raise DatoInvalido(f"{_id} no es una id válida")
        if isinstance(_nombre, str):
            self._nombre = _nombre
        else:
            raise DatoInvalido("Error: nombre no válido")
        if isinstance(_fabricante, str):
            self._fabricante = _fabricante
        else:
            raise DatoInvalido("Error: fabricante no válido")


    @property
    def id(self) -> str:
        return self._id
    @property
    def nombre(self) -> str:
        return self._nombre
    @property
    def fabricante(self) -> str:
        return self._fabricante

    @id.setter
    def id(self, valor : str):
        self._id = valor
    @nombre.setter
    def nombre(self, valor : str):
        self._nombre = valor
    @fabricante.setter
    def fabricante(self, valor : str):
        self._fabricante = valor

    def __str__(self) -> str:
        return f'{self._id}({self._nombre}) fabricante: {self._fabricante}'

    #Hago el método estático para probar mi manera al realizar la función estadísticas() pedida al final del punto 4
    @staticmethod
    @abstractmethod
    def tipo() -> str:
        pass