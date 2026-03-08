from LavadoraEstandar import LavadoraEstandar
from LavadoraInteligente import LavadoraInteligente


class SistemaLavaSmart:

    # Validar nombre
    def pedir_nombre(self):

        while True:

            try:

                nombre = input("Nombre del cliente: ").strip()

                if nombre == "":
                    print("El nombre no puede estar vacío")

                elif not nombre.replace(" ", "").isalpha():
                    print("El nombre solo debe contener letras")

                else:
                    return nombre

            except (EOFError, KeyboardInterrupt):

                print("\nOperación cancelada por el usuario")
                exit()

    # Validar kilos
    def pedir_kilos(self):

        while True:

            try:

                kilos = float(input("Peso de ropa en kilos (5 - 40): "))

                if kilos < 5 or kilos > 40:

                    print("Los kilos deben estar entre 5 y 40")

                else:

                    return kilos

            except ValueError:

                print("Debe ingresar un número válido")

            except (EOFError, KeyboardInterrupt):

                print("\nOperación cancelada")
                exit()

    # Validar tipo de ropa
    def pedir_tipo_ropa(self):

        tipos_validos = ["normal", "interior", "pijamas", "vestidos"]

        while True:

            try:

                tipo = input(
                    "Tipo de ropa (normal | interior | pijamas | vestidos): "
                ).lower()

                if tipo not in tipos_validos:

                    print("Tipo de ropa inválido")

                else:

                    return tipo

            except (EOFError, KeyboardInterrupt):

                print("\nOperación cancelada")
                exit()

    # Validar estrato
    def pedir_estrato(self):

        while True:

            try:

                estrato = int(input("Ingrese su estrato (2 - 5): "))

                if estrato not in [2, 3, 4, 5]:

                    print("Estrato inválido")

                else:

                    return estrato

            except ValueError:

                print("Debe ingresar un número")

            except (EOFError, KeyboardInterrupt):

                print("\nOperación cancelada")
                exit()

    # Tipo de lavadora
    def pedir_tipo_lavadora(self):

        while True:

            try:

                tipo = int(input("Tipo de lavadora (1 = Estándar | 2 = Inteligente): "))

                if tipo not in [1, 2]:

                    print("Opción inválida")

                else:

                    return tipo

            except ValueError:

                print("Ingrese 1 o 2")

            except (EOFError, KeyboardInterrupt):

                print("\nOperación cancelada")
                exit()

    # Sistema principal
    def iniciar(self):

        print("\n========= SISTEMA LAVA SMART =========\n")

        nombre = self.pedir_nombre()

        kilos = self.pedir_kilos()

        tipo_ropa = self.pedir_tipo_ropa()

        estrato = self.pedir_estrato()

        tipo_lavadora = self.pedir_tipo_lavadora()

        # Crear objeto según tipo (polimorfismo)

        if tipo_lavadora == 1:

            lavadora = LavadoraEstandar(kilos, tipo_ropa, estrato)

        else:

            lavadora = LavadoraInteligente(kilos, tipo_ropa, estrato)

        # Encender lavadora

        lavadora.encender()

        # Ejecutar ciclo completo

        lavadora.ciclo_terminado(nombre)