class Reserva:
    """
    Clase que representa una reserva realizada por un cliente.
    """

    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        if self.estado == "Cancelada":
            raise Exception("No se puede procesar una reserva cancelada.")

        costo = self.servicio.calcular_costo(self.duracion)
        self.estado = "Procesada"
        return costo

    def __str__(self):
        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )