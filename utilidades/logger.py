import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def registrar_evento(mensaje):
    """Registra un evento en el archivo de logs."""
    logging.info(mensaje)


def registrar_error(mensaje):
    """Registra un error en el archivo de logs."""
    logging.error(mensaje)