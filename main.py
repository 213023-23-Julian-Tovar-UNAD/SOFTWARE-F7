from modelos.cliente import Cliente
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria
from modelos.reserva import Reserva

from utilidades.logger import registrar_evento, registrar_error


def main():

    print("===== SOFTWARE FJ =====\n")

    # Listas
    clientes = []
    servicios = []
    reservas = []

    # -------------------------
    # Clientes
    # -------------------------

    try:
        cliente1 = Cliente("Julian Tovar", "12345", "julian@gmail.com")
        clientes.append(cliente1)
        registrar_evento("Cliente registrado correctamente.")
    except Exception as e:
        registrar_error(str(e))

    try:
        cliente2 = Cliente("Maria Perez", "54321", "maria@gmail.com")
        clientes.append(cliente2)
        registrar_evento("Cliente registrado correctamente.")
    except Exception as e:
        registrar_error(str(e))

    # Cliente inválido
    try:
        cliente3 = Cliente("Pedro", "88888", "correo_invalido")
        clientes.append(cliente3)
    except Exception as e:
        print("Error:", e)
        registrar_error(str(e))

    # -------------------------
    # Servicios
    # -------------------------

    sala = ReservaSala("Sala Premium", 50000, 20)
    equipo = AlquilerEquipo("Video Beam", 30000, "Proyector")
    asesoria = Asesoria("Asesoría Python", 80000, "Programación")

    servicios.extend([sala, equipo, asesoria])

    registrar_evento("Servicios creados correctamente.")

    # -------------------------
    # Reservas
    # -------------------------

    try:
        reserva1 = Reserva(cliente1, sala, 2)
        reservas.append(reserva1)

        reserva1.confirmar()

        total = reserva1.procesar()

        print(reserva1)
        print("Costo:", total)

    except Exception as e:
        registrar_error(str(e))

    try:
        reserva2 = Reserva(cliente2, equipo, 5)

        reservas.append(reserva2)

        reserva2.confirmar()

        total = reserva2.procesar()

        print(reserva2)
        print("Costo:", total)

    except Exception as e:
        registrar_error(str(e))

    try:
        reserva3 = Reserva(cliente1, asesoria, 3)

        reservas.append(reserva3)

        reserva3.confirmar()

        total = reserva3.procesar()

        print(reserva3)
        print("Costo:", total)

    except Exception as e:
        registrar_error(str(e))

    # -------------------------
    # Reserva inválida
    # -------------------------

    try:
        reserva4 = Reserva(cliente1, sala, -2)

    except Exception as e:
        print("Error:", e)
        registrar_error(str(e))

    # -------------------------
    # Cancelación
    # -------------------------

    try:

        reserva5 = Reserva(cliente2, sala, 1)

        reserva5.cancelar()

        reserva5.procesar()

    except Exception as e:
        print("Error:", e)
        registrar_error(str(e))

    # -------------------------
    # Mostrar servicios
    # -------------------------

    print("\n===== SERVICIOS =====")

    for servicio in servicios:
        print(servicio.descripcion())
        print("-------------------------")

    print("\nProyecto ejecutado correctamente.")


if __name__ == "__main__":
    main()