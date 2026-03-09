from SistemaLavaSmart import SistemaLavaSmart

# Librería que permite ejecutar comandos del sistema operativo
# En este caso se usa para simular el reinicio del sistema
import os

# FUNCIÓN PRINCIPAL DEL PROGRAMA
def main():
    # Permite atender múltiples clientes
    while True:
        
        try:

            # Se crea una instancia del sistema
            sistema = SistemaLavaSmart()

            # Se inicia el flujo completo del programa
            sistema.iniciar()

        # Manejo de interrupción si el usuario presiona CTRL + C
        except KeyboardInterrupt:

            print("\n\nSistema cancelado por el usuario.")
            return

        # Manejo de errores inesperados
        except Exception as error:

            print("\nError inesperado en el sistema:", error)
            
        
        # PREGUNTAR SI HAY OTRO CLIENTE
        while True:

            continuar = input('¿Desea usar la lavadora para otro cliente? ').lower()
            
            # Si el usuario quiere continuar
            if continuar == 's':
                
                # Simula reiniciar el sistema
                os.system("cls")  # limpia la pantalla en Windows

                print("\nReiniciando sistema...\n")

                break
            
            # Si el usuario decide terminar
            elif continuar == "n":

                print("\nSistema finalizado. Gracias por usar Lava Smart.")

                return

            # Si la entrada es inválida
            else:

                print("Entrada inválida. Solo escriba S o N.")

# PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":

    main()