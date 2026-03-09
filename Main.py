from SistemaLavaSmart import SistemaLavaSmart
import os


def main():
    while True:
        

        try:

            sistema = SistemaLavaSmart()

            sistema.iniciar()

        except KeyboardInterrupt:

            print("\n\nSistema cancelado por el usuario.")
            return

        except Exception as error:

            print("\nError inesperado en el sistema:", error)
            
        
        while True:
            continuar = input('¿Desea usar la lavadora para otro cliente?')
            
            if continuar == 's':
                
                os.system("\nReiniciando sitema...\n")
                break
            
            elif continuar == "n":

                print("\nSistema finalizado. Gracias por usar Lava Smart.")
                return

            else:

                print("Entrada inválida. Solo escriba S o N.")


if __name__ == "__main__":

    main()
    
    
