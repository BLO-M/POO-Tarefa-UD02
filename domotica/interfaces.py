from typing import Protocol, runtime_checkable

@runtime_checkable
class Medible(Protocol):
    def leer_valor(self) -> float: ...

@runtime_checkable
class Conmutable(Protocol):
    def activar(self) -> None: ...
    def desactivar(self) -> None: ...
    #Añadimos método para comprobar si el dispositivo está activado, también podríamos renombrar los atributos,
    # pero esto permite dejar nombres más coherentes con cada dispositivo
    def esta_activo(self) -> bool: ...

@runtime_checkable
class Actualizable(Protocol):
    def actualizar_firmware(self, version: str) -> None: ...