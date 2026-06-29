class ClienteInvalidoError(Exception):
    """Sale cuando un cliente tiene datos inválidos."""
    pass

class ServicioNoDisponibleError(Exception):
    """Sale cuando un servicio no está disponible."""
    pass

class ReservaError(Exception):
    """Sale cuando ocurre un error en una reserva."""
    pass

class DuracionInvalidaError(Exception):
    """Sale cuando la duración de una reserva no es válida."""
    pass

