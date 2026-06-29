from modelos.persona import Persona


class Cliente(Persona):
    """
    Clase que representa un cliente de Software FJ.
    """

    def __init__(self, nombre, documento, correo):
        super().__init__(nombre, documento)
        self.correo = correo

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        if "@" not in correo or "." not in correo:
            raise ValueError("Correo electrónico inválido.")
        self._correo = correo

    def __str__(self):
        return (
            f"Cliente: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}"
        )