from abc import ABC, abstractmethod



class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada


    def _validar_longitud(self, clave: str) -> bool:

        if len(clave) > self._longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        for c in clave:
            if c.isupper():
                return True
        else:
            return False

    def _contiene_minuscula(self, clave: str) -> bool:

        for c in clave:
            if c.islower():
                return True
        else:
            return False

    def _contiene_numero(self, clave: str) -> bool:
        for c in clave:
            if c.isdigit():
                return True
        else:
            return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):

    def contiene_caracter_especial(self):
        pass

    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):

    def contiene_calisto(self, clave: str) -> bool:
        pass

class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)