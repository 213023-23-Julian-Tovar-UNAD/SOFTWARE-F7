from modelos.cliente import Cliente
from modelos.reserva_sala import ReservaSala
from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria
from modelos.reserva import Reserva

from utilidades.logger import registrar_evento, registrar_error


def main():

    print("========== SOFTWARE FJ ==========")

    clientes = []
    servicios = []
    reservas = []

    contador = 0

    while contador < 10:

        print(f"\n========== OPERACIÓN {contador + 1} ==========")

        try:

            print("\n=== REGISTRO DEL CLIENTE ===")

            nombre = input("Nombre: ")

            # Validar documento
            while True:
                documento = input("Documento: ")

                if documento.isdigit():
                    break

                print("Error: El documento solo debe contener números.")
                registrar_error("Documento inválido.")

            # Validar correo
            while True:

                correo = input("Correo: ")

                try:
                    cliente = Cliente(nombre, documento, correo)
                    break

                except ValueError as e:
                    print("Error:", e)
                    registrar_error(str(e))
                    print("Ingrese nuevamente el correo.\n")

            clientes.append(cliente)
            registrar_evento("Cliente registrado correctamente.")

            # -------------------------
            # Servicios
            # -------------------------

            print("\n=== TIPOS DE SERVICIO ===")
            print("1. Reserva de Sala")
            print("2. Alquiler de Equipo")
            print("3. Asesoría")

            while True:

                opcion = input("Seleccione una opción: ")

                if opcion in ("1", "2", "3"):
                    break

                print("Error: Debe seleccionar una opción válida.")
                registrar_error("Opción de servicio inválida.")

            if opcion == "1":

                nombre_servicio = input("Nombre de la sala: ")

                while True:
                    try:
                        precio = float(input("Precio por hora: "))
                        break
                    except ValueError:
                        print("Ingrese un precio válido.")

                while True:
                    try:
                        capacidad = int(input("Capacidad: "))
                        break
                    except ValueError:
                        print("Ingrese una capacidad válida.")

                servicio = ReservaSala(nombre_servicio, precio, capacidad)

            elif opcion == "2":

                nombre_servicio = input("Nombre del equipo: ")

                while True:
                    try:
                        precio = float(input("Precio por día: "))
                        break
                    except ValueError:
                        print("Ingrese un precio válido.")

                tipo = input("Tipo de equipo: ")

                servicio = AlquilerEquipo(nombre_servicio, precio, tipo)

            elif opcion == "3":

                nombre_servicio = input("Nombre de la asesoría: ")

                while True:
                    try:
                        precio = float(input("Precio por hora: "))
                        break
                    except ValueError:
                        print("Ingrese un precio válido.")

                especialidad = input("Especialidad: ")

                servicio = Asesoria(nombre_servicio, precio, especialidad)

            servicios.append(servicio)
            registrar_evento("Servicio registrado correctamente.")

            # -------------------------
            # Reserva
            # -------------------------

            print("\n=== RESERVA ===")

            while True:

                try:

                    duracion = int(input("Duración: "))

                    if duracion <= 0:
                        print("La duración debe ser mayor que cero.")
                        continue

                    break

                except ValueError:
                    print("Debe ingresar un número entero.")
                    registrar_error("Duración inválida.")

            reserva = Reserva(cliente, servicio, duracion)

            reservas.append(reserva)

            reserva.confirmar()

            total = reserva.procesar()

        except Exception as e:

            print("\nError:", e)
            registrar_error(str(e))

        else:

            print("\n===== RESERVA EXITOSA =====")
            print(reserva)
            print(f"Costo total: ${total}")

        finally:

            contador += 1

            print(f"\nOperaciones realizadas: {contador}/10")

            if contador < 10:

                continuar = input("\n¿Desea realizar otra operación? (S/N): ").upper()

                if continuar != "S":
                    break

    print("\n========== RESUMEN ==========")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas realizadas: {len(reservas)}")

    print("\nGracias por utilizar Software FJ.")


if __name__ == "__main__":
    main()