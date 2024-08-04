# vehiculo.py

class Vehiculo:
    def __init__(self, marca, modelo, placa, tipo):
        self._marca = marca
        self._modelo = modelo
        self._placa = placa
        self._tipo = tipo
        self._estado = "Disponible"

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def placa(self):
        return self._placa

    @property
    def tipo(self):
        return self._tipo

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        self._estado = nuevo_estado

    def calcular_precio(self, dias):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

class Coche(Vehiculo):
    def calcular_precio(self, dias):
        base = 50 * dias
        return base + (1.5 * dias)

class Microbus(Vehiculo):
    def calcular_precio(self, dias):
        base = 50 * dias
        return base + (1.5 * dias) + 2

class FurgonetaCarga(Vehiculo):
    def calcular_precio(self, dias, pma=3):
        base = 50 * dias
        return base + (20 * pma)

class Camion(Vehiculo):
    def calcular_precio(self, dias, pma=5):
        base = 50 * dias
        return base + (20 * pma) + 40
