from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta para representar un servicio.
    """

    def __init__(self, nombre, precio_base):
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio_base = precio

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def descripcion(self):
        pass