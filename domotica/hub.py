from .dispositivos import *
from .interfaces import Conmutable, Medible
from .common import Duplicado

_dispositivos : dict[str, Dispositivo] = {}

def registrar(disp : Dispositivo):
    if disp.id not in _dispositivos:
        _dispositivos[disp.id] = disp
    else:
        raise Duplicado(f"El id {disp.id} ya está registrado en otro dispositivo")


def listar():
    return _dispositivos

def operar_todos():
    for disp in _dispositivos.values():
        if isinstance(disp, Medible):
            print(disp.__str__())
        if isinstance(disp, Conmutable):
            if disp.esta_activo():
                disp.desactivar()
            else:
                disp.activar()

def estadisticas() -> dict[str, int]:
    #Solo hice los métodos estáticos para ahorrarme el d.tipo(self) y hacerlo así, por probar distintos aspectos
    recuento : dict[str, int] = {d.tipo() : 0 for d in Dispositivo.__subclasses__()}
    for disp in _dispositivos.values():
        recuento[disp.tipo()] += 1
    return recuento
