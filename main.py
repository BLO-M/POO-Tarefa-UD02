from typing import TypedDict, NotRequired
from domotica import *


#Clase principalmente para tener contenta al IDE con los tipos, aunque si fuese a más el programa siempre es útil
class DefDispositivos(TypedDict):
    id: str
    tipo: str
    nombre: str
    fabricante: str
    temperatura: NotRequired[float]
    brillo: NotRequired[int]
    encendida: NotRequired[bool]
    activa: NotRequired[bool]


dispositivos_a_registrar : list[DefDispositivos]= [
    {"id" : "SOO1", "tipo" : "sensor", "nombre" : "Sensor cocina", "fabricante" : "Siemens", "temperatura" : 18},
    {"id" : "BOO1", "tipo" : "bombilla", "nombre" : "Bombilla entrada", "fabricante" : "IKEA", "brillo" : 90, "encendida" : False},
    {"id" : "COO1", "tipo" : "cerradura", "nombre" : "Cerradura entrada", "fabricante" : "Arregui", "activa" : True},
    {"id" : "S002", "tipo" : "sensor", "nombre" : "Sensor exterior", "fabricante" : "Luz Negra>", "temperatura" : 12},
    {"id" : "B002", "tipo" : "bombilla", "nombre" : "Bombilla habitación", "fabricante" : "Simon", "brillo" : 40, "encendida" : True},
    {"id" : "C002", "tipo" : "cerradura", "nombre" : "Cerradura garaje", "fabricante" : "JIS>", "activa" : True},
    {"id" : "003", "tipo" : "sensor", "nombre" : "Sensor habitación", "fabricante" : "Siemens", "temperatura" : 20},
    {"id" : "B002", "tipo" : "bombilla", "nombre" : "Bombilla sótano", "fabricante" : "WiZ", "brillo" : 60, "encendida" : False},
]


print("Iniciando demo de sistema de robótica...")
#No instancio hub porque no vi la necesidad de que fuese una clase.

print("Validando e instanciando:\n")
for disp in dispositivos_a_registrar:
    match disp["tipo"]:
        case "sensor":
            try:
                #El ID se valida en el constructor de Dispositivo
                hub.registrar(SensorTemperatura(disp["id"], disp["nombre"], disp["fabricante"], disp["temperatura"]))
            except DatoInvalido as e:
                print(f"Error: {e}")
            except Duplicado as e:
                print(f"Error: {e}")
            else:
                print(f"OK: ´{disp["id"]}({disp["tipo"]})->SensorTemperatura\"{disp["nombre"]}\"({disp["fabricante"]}, {disp["temperatura"]})")
        case "bombilla":
            try:
                hub.registrar(BombillaInteligente(disp["id"], disp["nombre"], disp["fabricante"], disp["brillo"], disp["encendida"]))
            except DatoInvalido as e:
                print(f"Error: {e}")
            except Duplicado as e:
                print(f"Error: {e}")
            else:
                print(f"OK: ´{disp["id"]}({disp["tipo"]})->BombillaInteligente\"{disp["nombre"]}\"({disp["fabricante"]}, brillo={disp["brillo"]})")
        case "cerradura":
            try:
                hub.registrar(CerraduraInteligente(disp["id"], disp["nombre"], disp["fabricante"], disp["activa"]))
            except DatoInvalido as e:
                print(f"Error: {e}")
            except Duplicado as e:
                print(f"Error: {e}")
            else:
                print(f"OK: ´{disp["id"]}({disp["tipo"]})->CerraduraInteligente\"{disp["nombre"]}\"({disp["fabricante"]}"
                      f", {'bloqueada' if disp["activa"] else 'desbloqueada'})")

print(f"\nRegistro en Hub completado: {len(hub.listar())} dispositivos")

print("\nListado de dispositivos:\n")
for disp in hub.listar().values():
    print(disp.__str__())

print("\nCapacidades detectadas:\n")
for disp in hub.listar().values():
    capacidades = disp.id + " ->"
    if isinstance(disp, Medible):
        capacidades += " Medible"
    if isinstance(disp, Conmutable):
        if capacidades[-1] != 'e':
            capacidades += ','
        capacidades += " Conmutable"
    if isinstance(disp, Actualizable):
        if capacidades[-1] != 'e':
            capacidades += ','
        capacidades += " Actualizable"

    print(capacidades)

print("\nOperar todos, polimorfismo:\n")
for disp in hub.listar().values():
    operacion = disp.id + " -> "
    if isinstance(disp, Medible):
        operacion += f" temperatura: {disp.leer_valor()}ºC "
    if isinstance(disp, Conmutable):
        operacion += f" activo(inicial, encender, apagar) = {disp.esta_activo()}"
        disp.activar()
        operacion += f", {disp.esta_activo()}"
        disp.desactivar()
        operacion += f", {disp.esta_activo()}"

    print(operacion)

print("\nAcciones específicas:\n")
#Localizamos un dispositivo de cada
bombilla : BombillaInteligente | None = None
cerradura : CerraduraInteligente | None = None
for disp in hub.listar().values():
    if disp.tipo() == "BombillaInteligente" and bombilla is None:
        bombilla = disp
        if cerradura is not None:
            break
    elif disp.tipo() == "CerraduraInteligente" and cerradura is None:
        cerradura = disp
        if bombilla is not None:
            break
if bombilla is not None:
    brilloAnterior = bombilla.brillo
    bombilla.brillo = 1
    print(f"La bombilla {bombilla.id} cuyo brillo era {brilloAnterior}, ha cambiado a {bombilla.brillo}")
    #No se ha implementado, ni indicado como, la interfaz Actualizable ni ningún atributo que indique su versión
if cerradura is not None:
    abrilCerral = f"Cerradura {cerradura.id} activa(actual, bloquear(), desbloquear(), bloquear())-> {cerradura.esta_activo()}"
    cerradura.activar()
    abrilCerral += f", {cerradura.esta_activo()}"
    cerradura.desactivar()
    abrilCerral += f", {cerradura.esta_activo()}"
    cerradura.activar()
    abrilCerral += f", {cerradura.esta_activo()}"
    print(abrilCerral)

print("\nEstadísticas:\n")
for c, v in hub.estadisticas().items():
    print(f"{c}: {v}")

print("\nResumen de capacidades:\n")
medible = conmutable = actualizable = 0
for disp in hub.listar().values():
    if isinstance(disp, Medible):
        medible += 1
    if isinstance(disp, Conmutable):
        conmutable += 1
    if isinstance(disp, Actualizable):
        actualizable += 1
print(f"Medibles: {medible}")
print(f"Conmutables: {conmutable}")
print(f"Actualizables: {actualizable}")

print("\nPruebas de errores controlados:\n")
try:
    print("Registramos de nuevo el id SOO1")
    # noinspection SpellCheckingInspection
    duplicado = SensorTemperatura("SOO1", "duplicidad", "Ziemenz", 60)
    hub.registrar(duplicado)
except Duplicado as e:
    print(e)

#No se ha implementado, ni indicado como, la interfaz Actualizable ni ningún atributo que indique su versión

try:
    try:
        print("Buscamos el dispositivo inexistente con id B999")
        print(hub.listar()["B999"].__str__())
    except KeyError as e:
        raise NoEncontrado(f"Dispositivo {e} no encontrado")
except NoEncontrado as e:
    print(e)

print("\nFIN DE LA DEMO")