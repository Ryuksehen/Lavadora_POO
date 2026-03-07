import time
from SonidosLavadora import SonidosLavadora


class LavadoraBase:

    # -----------------------------
    # Constantes del sistema
    # -----------------------------

    PRECIO_KILO = 10000
    AUMENTO_ESPECIAL = 0.05
    IVA = 0.19

    POTENCIA_KW = 1.2

    TARIFAS_ESTRATO = {
        2: 867.8,
        3: 737.6,
        4: 867.8,
        5: 1041
    }

    PRENDAS_ESPECIALES = ["interior", "pijamas", "vestidos"]

    # -----------------------------
    # Constructor
    # -----------------------------

    def __init__(self, kilos, tipo_ropa, estrato, tipo_lavadora="estandar"):

        self._kilos = kilos
        self._tipo_ropa = tipo_ropa
        self._estrato = estrato

        self._tipo_lavadora = tipo_lavadora

        self._tiempo_lavado = 20

        self.__estado = "apagada"

        self._ultimo_sonido = None

    # -----------------------------
    # Encender lavadora
    # -----------------------------

    def encender(self):

        if self.__estado == "encendida":
            print("La lavadora ya está encendida")
            return

        self.__estado = "encendida"

        SonidosLavadora.encender(self._tipo_lavadora)

    # -----------------------------
    # Validación kilos
    # -----------------------------

    def _validar_kilos(self):

        if self._kilos < 5 or self._kilos > 40:
            raise ValueError("Los kilos deben estar entre 5 y 40")

    # -----------------------------
    # Llenado del tanque
    # -----------------------------

    def _llenar(self):

        print("\nIniciando llenado del tanque...")

        SonidosLavadora.llenado(self._tipo_lavadora)
        self._ultimo_sonido = "llenado"

        for i in range(3):

            print("💧 Llenando agua...", i + 1)

            time.sleep(1)

        print("Tanque lleno")

    # -----------------------------
    # Control del ciclo
    # -----------------------------

    def _control_ciclo(self):

        while True:

            print("\nControl de ciclo")

            print("1. Continuar")
            print("2. Pausar")
            print("3. Finalizar ciclo")

            try:

                opcion = input("Seleccione una opción: ")

            except (EOFError, KeyboardInterrupt):

                print("\nOperación cancelada por el usuario")

                return "finalizar"

            if opcion == "1":

                return "continuar"

            elif opcion == "2":

                self.__estado = "pausada"

                SonidosLavadora.pausa(self._tipo_lavadora)

                print("\nLavadora en pausa")

                print("1. Reanudar")
                print("2. Finalizar ciclo")

                op = input("Seleccione opción: ")

                if op == "1":

                    self.__estado = "lavando"

                    SonidosLavadora.reanudar(self._tipo_lavadora)

                    if self._ultimo_sonido:

                        SonidosLavadora.reproducir(self._tipo_lavadora, self._ultimo_sonido)

                    return "continuar"

                else:

                    print("Ciclo cancelado")

                    return "finalizar"

            elif opcion == "3":

                print("Ciclo cancelado por el usuario")

                return "finalizar"

            else:

                print("Opción inválida")

    # -----------------------------
    # Simulación del tambor
    # -----------------------------

    def _simular_tambor(self):

        self.__estado = "lavando"

        for ciclo in range(5):

            print("\n🌀 Girando tambor... ciclo", ciclo + 1)

            SonidosLavadora.lavado(self._tipo_lavadora)
            self._ultimo_sonido = "lavado"

            time.sleep(1)

            estado = self._control_ciclo()

            if estado == "finalizar":

                return False

        return True

    # -----------------------------
    # Lavado (polimorfismo)
    # -----------------------------

    def lavar(self):

        raise NotImplementedError("Debe ser implementado por las clases hijas")

    # -----------------------------
    # Enjuague
    # -----------------------------

    def _enjuagar(self):

        print("\nIniciando enjuague")

        SonidosLavadora.enjuague(self._tipo_lavadora)
        self._ultimo_sonido = "enjuague"

        time.sleep(2)

        print("Ropa enjuagada")

    # -----------------------------
    # Secado
    # -----------------------------

    def _secar(self):

        print("\nIniciando secado")

        SonidosLavadora.secado(self._tipo_lavadora)
        self._ultimo_sonido = "secado"

        time.sleep(3)

        print("Ropa seca")

    # -----------------------------
    # Cálculo de costos
    # -----------------------------

    def __calcular_costos(self):

        costo_base = self._kilos * self.PRECIO_KILO

        if self._tipo_ropa in self.PRENDAS_ESPECIALES:

            costo_base *= (1 + self.AUMENTO_ESPECIAL)

        costo_con_iva = costo_base * (1 + self.IVA)

        utilidad = costo_base * 0.30

        return costo_base, costo_con_iva, utilidad

    # -----------------------------
    # Cálculo consumo energía
    # -----------------------------

    def __calcular_consumo_energia(self):

        tarifa = self.TARIFAS_ESTRATO.get(self._estrato)

        kwh = self.POTENCIA_KW * (self._tiempo_lavado / 60)

        costo = kwh * tarifa

        return costo

    # -----------------------------
    # Reporte cliente
    # -----------------------------

    def _mostrar_reporte_cliente(self, nombre):

        costo_base, costo_final, utilidad = self.__calcular_costos()

        energia = self.__calcular_consumo_energia()

        print("\n========== REPORTE CLIENTE ==========")

        print("Cliente:", nombre)
        print("Kilos lavados:", self._kilos)
        print("Tipo de prenda:", self._tipo_ropa)

        print("Costo base:", round(costo_base, 2))
        print("Total con IVA:", round(costo_final, 2))
        print("Costo energía:", round(energia, 2))

        print("Utilidad empresa:", round(utilidad, 2))

        print("\nGracias por usar Lava Smart")

    # -----------------------------
    # Ciclo completo
    # -----------------------------

    def ciclo_terminado(self, nombre):

        try:

            self._validar_kilos()

            self._llenar()

            continuar = self.lavar()

            if continuar is False:

                return

            self._enjuagar()

            try:

                secar = input("¿Desea secar la ropa? (s/n): ")

            except (EOFError, KeyboardInterrupt):

                print("\nProceso interrumpido")

                return

            if secar.lower() == "s":

                self._secar()

            SonidosLavadora.fin(self._tipo_lavadora)

            print("\nGenerando reportes...\n")

            self._mostrar_reporte_cliente(nombre)

        except (EOFError, KeyboardInterrupt):

            print("\nSistema detenido por el usuario")

        except Exception as e:

            print("Error en el ciclo:", e)