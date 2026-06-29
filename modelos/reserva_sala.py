from modelos.servicio import Servicio


class ReservaSala(Servicio):
    """
    Servicio de reserva de salas.
    """

    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        """
        Calcula el costo de la reserva.
        Se usan parámetros opcionales para simular sobrecarga.
        """
        total = self.precio_base * horas
        total = total - descuento + impuesto
        return total

    def descripcion(self):
        return (
            f"Servicio: {self.nombre}\n"
            f"Capacidad: {self.capacidad} personas\n"
            f"Precio por hora: ${self.precio_base}"
        )