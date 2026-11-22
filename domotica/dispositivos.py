from .base import Dispositivo

class SensorTemperatura(Dispositivo):
    def __init__(self, _id: str, _nombre: str, _fabricante: str, _celsius: float):
        super().__init__(_id, _nombre, _fabricante)
        self._celsius = _celsius

    def leer_valor(self):
        return self._celsius

    # Hago el método estático para probar mi manera al realizar la función estadísticas() pedida al final del punto 4
    @staticmethod
    def tipo() -> str:
        return "SensorTemperatura"

    def __str__(self) -> str:
        return f"{super().__str__()} temperatura:{str(self._celsius)}ºC"


class BombillaInteligente(Dispositivo):
    def __init__(self, _id: str, _nombre: str, _fabricante: str, _brillo : int, _encendida : bool):
        super().__init__(_id, _nombre, _fabricante)
        if 0 <= _brillo <= 100:
            self._brillo = _brillo
        self._encendida = _encendida

    def encender(self):
        self._encendida = True
    def apagar(self):
        self._encendida = False
    #Adaptamos para encajar encender y apagar con el Protocol Conmutable
    def activar(self):
        self.encender()
    def desactivar(self):
        self.apagar()

    def esta_activo(self) -> bool:
        return self._encendida

    # Hago el método estático para probar mi manera al realizar la función estadísticas() pedida al final del punto 4
    @staticmethod
    def tipo() -> str:
        return "BombillaInteligente"

    def __str__(self) -> str:
        return f"{super().__str__()} brillo:{str(self._brillo)} encendida:{str(self._encendida)}"

    @property
    def brillo(self) -> int:
        return self._brillo

    @brillo.setter
    def brillo(self, _brillo : int):
        self._brillo = _brillo


class CerraduraInteligente(Dispositivo):
    def __init__(self, _id : str, _nombre : str, _fabricante : str, _bloqueada : bool):
        super().__init__(_id, _nombre, _fabricante)
        self._bloqueada = _bloqueada

    def bloquear(self):
        self._bloqueada = True
    def desbloquear(self):
        self._bloqueada = False
    #Adaptamos para encajar bloquear y desbloquear con el Protocol Conmutable
    def activar(self):
        self.bloquear()
    def desactivar(self):
        self.desbloquear()

    def esta_activo(self) -> bool:
        return self._bloqueada

    # Hago el método estático para probar mi manera al realizar la función estadísticas() pedida al final del punto 4
    @staticmethod
    def tipo() -> str:
        return "CerraduraInteligente"

    def __str__(self) -> str:
        return f"{super().__str__()} bloqueada:{str(self._bloqueada)}"
