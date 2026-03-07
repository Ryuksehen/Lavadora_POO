from SistemaLavaSmart import SistemaLavaSmart


def main():

    try:

        sistema = SistemaLavaSmart()

        sistema.iniciar()

    except KeyboardInterrupt:

        print("\n\nSistema cancelado por el usuario.")

    except Exception as error:

        print("\nError inesperado en el sistema:", error)


if __name__ == "__main__":

    main()
    
    
