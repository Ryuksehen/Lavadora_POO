from LavadoraEstandar import LavadoraEstandar
from LavadoraInteligente import LavadoraInteligente

#  SISTEMA LAVA SMART
class SistemaLavaSmart:
    def __init__(self):

        # Estadísticas del sistema
        self.total_clientes = 0
        self.total_lavados = 0
        self.total_kilos = 0

        self.total_cobrado = 0
        self.total_iva = 0
        self.total_ganancia = 0

        self.total_energia = 0
        self.total_agua = 0

        self.lavados_estandar = 0
        self.lavados_inteligentes = 0
        
        self.wifi_cliente = False

        self.tipos_ropa = {
            "normal": 0,
            "interior": 0,
            "pijamas": 0,
            "vestidos": 0
        }

        self.recargos = {
            "interior": 0,
            "pijamas": 0,
            "vestidos": 0
        }

    # VALIDAR NOMBRE DEL CLIENTE
    def pedir_nombre(self):

        while True:

            try:

                nombre = input("Nombre del cliente: ").strip()

                # Verifica si el nombre está vacío
                if nombre == "":
                    print("El nombre no puede estar vacío")

                # Verifica que solo tenga letras
                elif not nombre.replace(" ", "").isalpha():
                    print("El nombre solo debe contener letras")

                else:
                    return nombre

            except (EOFError, KeyboardInterrupt):

                print("\nOperación cancelada por el usuario")
                exit()

    # VALIDAR TIPO DE ROPA
    def pedir_tipo_ropa(self):

        mapa = {
            "n": "normal",
            "i": "interior",
            "p": "pijamas",
            "v": "vestidos"
        }

        prendas = []

        print("\nSeleccione los tipos de ropa que desea lavar")

        while True:

            opcion = input(
                "\nN → Normal\n"
                "I → Interior\n"
                "P → Pijamas\n"
                "V → Vestidos\n"
                "X → Terminar selección\n"
                "Seleccione: "
            ).strip().lower()

            if opcion == "x":

                if len(prendas) == 0:
                    print("Debe seleccionar al menos un tipo de ropa")
                    continue

                return prendas

            if opcion in mapa:

                tipo = mapa[opcion]

                # pedir kilos para ese tipo
                while True:

                    try:

                        kilos = float(
                            input(f"Ingrese kilos para {tipo} (1 - 40): ")
                        )

                        if kilos <= 0 or kilos > 40:
                            print("Cantidad inválida")
                            continue

                        prendas.append((tipo, kilos))

                        print(f"{tipo} agregado con {kilos} kg")

                        break

                    except ValueError:
                        print("Debe ingresar un número")

            else:

                print("Opción inválida")
                
                
    # VALIDAR ESTRATO
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


    # SELECCIONAR TIPO DE LAVADORA
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


    # SISTEMA PRINCIPAL
    def iniciar(self):

        print("\n" + "="*40)
        print("        SISTEMA LAVA SMART")
        print("="*40)

        # Solicita los datos del cliente
        nombre = self.pedir_nombre()

        tipo_ropa = self.pedir_tipo_ropa()

        estrato = self.pedir_estrato()

        tipo_lavadora = self.pedir_tipo_lavadora()
        
        lavados_cliente = []

        # CREACIÓN DEL OBJETO 
        for ropa, kilos in tipo_ropa:

            print(f"\nPreparando lavado para {ropa} ({kilos} kg)")

            if tipo_lavadora == 1:

                lavadora = LavadoraEstandar(kilos, ropa, estrato)

            else:

                lavadora = LavadoraInteligente(kilos, ropa, estrato)
                lavadora._wifi = self.wifi_cliente

            lavadora.encender()

            datos = lavadora.ciclo_terminado(nombre)
            self.wifi_cliente = lavadora._wifi

            if datos:

                lavados_cliente.append((ropa, kilos))

                self.registrar_lavado({
                    "tipo_ropa": ropa,
                    "kilos": kilos,
                    "metodo": datos["metodo"],
                    "total": 0,
                    "iva": 0,
                    "ganancia": 0,
                    "energia": 0,
                    "recargo": 0
                })
                
        self.generar_reporte_cliente(nombre, lavados_cliente)
        
    def generar_reporte_cliente(self, nombre, lavados):

        print("\n" + "="*50)
        print("              REPORTE CLIENTE")
        print("="*50)

        print(f"Cliente : {nombre}")

        print("\nPrendas lavadas:")

        kilos_totales = 0

        for ropa, kilos in lavados:

            print(f" - {ropa} : {int(kilos)} kg")
            kilos_totales += kilos

        print(f"\nKilos totales : {int(kilos_totales)} kg")

        costo_base = kilos_totales * 10000
        iva = costo_base * 0.19
        total = costo_base + iva

        print("-"*50)
        print(f"Costo base : ${costo_base:,.2f}")
        print(f"IVA (19%)  : ${iva:,.2f}")
        print("-"*50)
        print(f"TOTAL      : ${total:,.2f}")
        print("="*50)
                    
    
    def registrar_lavado(self, datos):
        self.total_lavados += 1
        self.total_clientes += 1
        self.total_kilos += datos["kilos"]

        self.total_cobrado += datos["total"]
        self.total_iva += datos["iva"]
        self.total_ganancia += datos["ganancia"]

        self.total_energia += datos["energia"]

        # Agua estimada
        self.total_agua += datos["kilos"] * 10

        # Tipo de ropa
        self.tipos_ropa[datos["tipo_ropa"]] += 1

        # Recargos
        if datos["tipo_ropa"] in self.recargos:
            self.recargos[datos["tipo_ropa"]] += datos["recargo"]

        # Tipo de lavadora
        if datos["metodo"] == "Estándar":
            self.lavados_estandar += 1
        else:
            self.lavados_inteligentes += 1
            
    def mostrar_reporte_admin(self):
            
            print("\n" + "="*55)
            print("           REPORTE ADMINISTRADOR")
            print("="*55)

            print("\nOPERACIÓN")
            print("-"*55)
            print(f"Clientes atendidos        : {self.total_clientes}")
            print(f"Lavados realizados        : {self.total_lavados}")
            print(f"Kilos totales             : {self.total_kilos} kg")

            print("\nTIPOS DE LAVADORA")
            print("-"*55)
            print(f"Estándar                  : {self.lavados_estandar}")
            print(f"Inteligente               : {self.lavados_inteligentes}")

            print("\nTIPOS DE ROPA")
            print("-"*55)

            for tipo, cantidad in self.tipos_ropa.items():
                print(f"{tipo.capitalize():25}: {cantidad}")

            print("\nRECURSOS UTILIZADOS")
            print("-"*55)
            print(f"Energía usada             : {self.total_energia:.2f} kWh")
            print(f"Agua utilizada            : {self.total_agua} litros")

            print("\nFINANZAS")
            print("-"*55)
            print(f"Total cobrado             : ${self.total_cobrado:,.2f}")
            print(f"IVA cobrado               : ${self.total_iva:,.2f}")
            print(f"Ganancia estimada         : ${self.total_ganancia:,.2f}")

            print("\nRECARGOS POR PRENDA")
            print("-"*55)

            total_recargos = 0

            for tipo, valor in self.recargos.items():

                print(f"{tipo.capitalize():25}: ${valor:,.2f}")
                total_recargos += valor

            print(f"\nTotal recargos            : ${total_recargos:,.2f}")

            print("="*55)