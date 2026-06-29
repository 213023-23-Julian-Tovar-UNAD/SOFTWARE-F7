class ClienteInvalidoError(Exception):
    """Se lanza cuando un cliente tiene datos inválidos."""
    pass


class ServicioNoDisponibleError(Exception):
    """Se lanza cuando un servicio no está disponible."""
    pass


class ReservaError(Exception):
    """Se lanza cuando ocurre un error en una reserva."""
    pass


class DuracionInvalidaError(Exception):
    """Se lanza cuando la duración de una reserva no es válida."""
    pass