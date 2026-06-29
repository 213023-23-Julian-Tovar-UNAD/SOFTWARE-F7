from modelos.servicio import Servicio


class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos.
    """

    def __init__(self, nombre, precio_base, tipo_equipo):
        super().__init__(nombre, precio_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias, descuento=0, impuesto=0):
        """
        Calcula el costo del alquiler por días.
        """
        total = self.precio_base * dias
        total = total - descuento + impuesto
        return total

    def descripcion(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Tipo de equipo: {self.tipo_equipo}\n"
            f"Precio por día: ${self.precio_base}"
        )