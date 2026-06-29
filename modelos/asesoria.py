from modelos.servicio import Servicio


class Asesoria(Servicio):
    """
    Servicio de asesoría especializada.
    """

    def __init__(self, nombre, precio_base, especialidad):
        super().__init__(nombre, precio_base)
        self.especialidad = especialidad

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        """
        Calcula el costo de la asesoría por horas.
        """
        total = self.precio_base * horas
        total = total - descuento + impuesto
        return total

    def descripcion(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Especialidad: {self.especialidad}\n"
            f"Precio por hora: ${self.precio_base}"
        )