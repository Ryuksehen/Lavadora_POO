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

        mapa = {
            "n": "normal",
            "normal": "normal",
            "i": "interior",
            "interior": "interior",
            "p": "pijamas",
            "pijamas": "pijamas",
            "v": "vestidos",
            "vestidos": "vestidos"
        }

        while True:

            try:

                tipo = input(
                    "\nTipo de ropa\n"
                    "N → Normal\n"
                    "I → Interior\n"
                    "P → Pijamas\n"
                    "V → Vestidos\n"
                    "Seleccione: "
                ).strip().lower()

                if tipo in mapa:
                    return mapa[tipo]

                print("Tipo de ropa inválido. Introduce un valor valido.")

            except (EOFError, KeyboardInterrupt):

                print("\nEntrada cancelada. Intente nuevamente.")
                continue

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

                tipo = input(
                    "Tipo de lavadora (1 = Estándar | 2 = Inteligente: "
                ).strip().lower()

                if tipo in ["1", "e"]:
                    return 1

                elif tipo in ["2", "i"]:
                    return 2

                else:
                    print("Opción inválida. Introduce un valor valido.")

            except (EOFError, KeyboardInterrupt):

                print("\nEntrada cancelada. Intente nuevamente.")
                continue

    # Sistema principal
    def iniciar(self):

        print("\n" + "="*40)
        print("        SISTEMA LAVA SMART")
        print("="*40)

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