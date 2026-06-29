from abc import ABC


class Persona(ABC):
    """
    Clase abstracta que representa una persona del sistema.
    """

    def __init__(self, nombre, documento):
        self._nombre = nombre
        self._documento = documento

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, documento):
        if not str(documento).isdigit():
            raise ValueError("El documento debe contener solo números.")
        self._documento = documento

    def __str__(self):
        return f"Nombre: {self._nombre} | Documento: {self._documento}"