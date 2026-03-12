from SistemaLavaSmart import SistemaLavaSmart
import os


def main():

    # Se crea UNA sola instancia del sistema
    sistema = SistemaLavaSmart()

    while True:

        try:

            # Se ejecuta un lavado
            sistema.iniciar()

        except KeyboardInterrupt:

            print("\n\nSistema cancelado por el usuario.")
            break

        except Exception as error:

            print("\nError inesperado en el sistema:", error)

        # PREGUNTAR SI HAY OTRO CLIENTE
        while True:

            continuar = input('¿Desea usar la lavadora para otro cliente? ').lower()

            if continuar == 's':

                os.system("cls")
                print("\nReiniciando sistema...\n")

                break

            elif continuar == "n":

                # AQUÍ mostramos el reporte administrador
                sistema.mostrar_reporte_admin()

                print("\nSistema finalizado. Gracias por usar Lava Smart.")
                return

            else:

                print("Entrada inválida. Solo escriba S o N.")


if __name__ == "__main__":

    main()