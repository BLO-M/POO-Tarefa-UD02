
class DatoInvalido(ValueError):
    #Un dato no cumple el formato o las reglas de negocio
    #Ejemplo de mensaje: 'ID generado inválido: 'B00-
    pass

class Duplicado(Exception):
    #Se intenta registrar/insertar un elemento con clave ya existente (validado en Hub)
    #Ejemplo de mensaje: "El ID 'B001' ya existe"
    pass

class NoEncontrado(Exception):
    #No existe un elemento solicitado por su identificador
    #Ejemplo de mensaje: "No existe el dispositivo 'X999'"
    pass


class Utils:
    #No necesito self ni dependen de ninguna instancia, así que hago las funciones estáticas
    @staticmethod
    def validar_id(texto) -> bool:
        if not isinstance(texto, str):
            return False
        txt = texto.strip()
        if txt == "":
            return False
        if not txt[0].isalpha():
            return False

        return all(char.isalnum() or char == '-' for char in txt)

    @staticmethod
    def fabricar_id(prefijo : str, n : int) -> str:
        if not isinstance(prefijo, str):
            raise DatoInvalido("Prefijo no válido")
        prefijo = prefijo.strip()
        if not prefijo.isalpha():
            raise DatoInvalido("Prefijo no válido")
        prefijo = prefijo.upper()
        if not isinstance(n, int) or n < 100 or n > 999:
            raise DatoInvalido("Número no válido")
        #El ejercicio menciona que puede haber ceros a la izquierda, pero eso no se puede si lo que se pasa es un int

        res = prefijo + str(n)
        if not Utils.validar_id(res):
            raise DatoInvalido(f"ID generado inválido: {res}")
        return res

    @staticmethod
    def validar_version(version : str) -> bool:
        pass
