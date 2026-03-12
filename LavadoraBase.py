# Importa la clase que controla todos los sonidos de la lavadora
from SonidosLavadora import SonidosLavadora

# Librería para simular tiempos reales como las pausas del sistema)
import time  

# Permite obtener la fecha y hora actual para el reporte
from datetime import datetime  

# Librería de Windows para leer teclas del teclado sin presionar ENTER
import msvcrt  

# Clase que se encarga de generar los archivos de reportes (TXT y Excel)
from Reportes import Reportes  

class LavadoraBase:

    # CONSTANTES DEL SISTEMA

    # Precio por kilo de ropa
    PRECIO_KILO = 10000

    # Aumento del 5% para prendas especiales
    AUMENTO_ESPECIAL = 0.05

    # IVA del servicio
    IVA = 0.19

    # Potencia de la lavadora en kilovatios
    POTENCIA_KW = 1.2

    # Tarifas de energía según el estrato
    TARIFAS_ESTRATO = {
        2: 867.8,
        3: 737.6,
        4: 867.8,
        5: 1041
    }

    # Lista de prendas que generan recargo
    PRENDAS_ESPECIALES = ["interior", "pijamas", "vestidos"]

    def __init__(self, kilos, tipo_ropa, estrato, tipo_lavadora="estandar"):
        self._kilos = kilos
        self._tipo_ropa = tipo_ropa
        self._estrato = estrato
        self._tipo_lavadora = tipo_lavadora
        self._tiempo_lavado = 20
        self.__estado = "apagada"
        # Nuevas variable
        self._ultimo_sonido = None # Lo guarda para que suene el ultimo sondios que se reprodujo antes de pausar
        self._lavados_cliente = []


    # Lee una tecla del teclado
    def _leer_tecla(self):

        tecla = msvcrt.getch()

        if tecla == b'\r' or tecla == b'1':
            return "continuar"

        elif tecla == b'\t' or tecla == b'2':
            return "pausar"

        elif tecla == b'\x1b' or tecla == b'3':
            return "finalizar"

        else:
            return "otra"


    # Valida respuestas tipo S / N 
    def _validar_sn(self, pregunta):

        while True:

            respuesta = input(pregunta).strip().lower()

            if respuesta in ["s", "n"]:
                return respuesta

            print("Entrada inválida. Solo escriba S o N.")


    # ENCENDER LAVADORA
    def encender(self):

        # Verifica si ya está encendida
        if self.__estado == "encendida":
            print("La lavadora ya está encendida")
            return

        # Cambia el estado
        self.__estado = "encendida"

        # Reproduce sonido de encendido
        SonidosLavadora.encender(self._tipo_lavadora)

        print("Seleccionando programa de lavado...")

        # Sonido de selección de programa
        SonidosLavadora.seleccionar_programa(self._tipo_lavadora)


    # VALIDACIÓN DE KILOS
    def _validar_kilos(self):

        # La lavadora solo acepta entre 5 y 40 kilos
        if self._kilos < 5 or self._kilos > 40:
            raise ValueError("Los kilos deben estar entre 5 y 40")


    # LLENADO DE AGUA
    def _llenar(self):

        print("\nIniciando llenado del tanque...")

        # Sonido del agua llenando
        SonidosLavadora.llenado(self._tipo_lavadora)

        self._ultimo_sonido = "llenado"

        # Simulación del llenado
        for i in range(3):

            print("Llenando agua...", i + 1)
            time.sleep(1)

        print("Tanque lleno")


    # CONTROL DEL CICLO 
    def _control_ciclo(self):

        print("\nControles:")
        print("1  → Continuar")
        print("2  → Pausar")
        print("3  → Finalizar")

        accion = self._leer_tecla()

        if accion == "continuar":
            return "continuar"

        elif accion == "pausar":

            # Cambia el estado a pausado
            self.__estado = "pausada"

            SonidosLavadora.pausa(self._tipo_lavadora)

            print("\n⏸ Lavadora en pausa")
            print("1  → Reanudar")
            print("3     → Cancelar")

            while True:

                accion = self._leer_tecla()

                if accion == "continuar":

                    self.__estado = "lavando"

                    SonidosLavadora.reanudar(self._tipo_lavadora)

                    # Reproduce el último sonido que estaba activo
                    if self._ultimo_sonido:
                        SonidosLavadora.reproducir(
                            self._tipo_lavadora,
                            self._ultimo_sonido
                        )

                    return "continuar"

                elif accion == "finalizar":

                    print("Ciclo cancelado")
                    return "finalizar"

        elif accion == "finalizar":

            print("Ciclo cancelado por el usuario")
            return "finalizar"


    # SIMULACIÓN DEL TAMBOR
    def _simular_tambor(self):

        self.__estado = "lavando"
        
        print("\nIniciando ciclo de lavado...")

        SonidosLavadora.inicioLavado(self._tipo_lavadora)

        # Simula 5 ciclos de giro
        for ciclo in range(5):

            print("\n Girando tambor... ciclo", ciclo + 1)

            SonidosLavadora.lavado(self._tipo_lavadora)

            self._ultimo_sonido = "lavado"

            time.sleep(1)

            # Permite controlar pausa o cancelación
            estado = self._control_ciclo()

            if estado == "finalizar":
                return False

        print("\nDrenando agua...")

        SonidosLavadora.drenado(self._tipo_lavadora)

        time.sleep(2)

        return True


    def lavar(self):
        raise NotImplementedError(
            "Debe ser implementado por las clases hijas"
        )


    # ENJUAGUE
    def _enjuagar(self):

        respuesta = self._validar_sn("\n¿Desea enjuagar la ropa? (s/n): ")

        if respuesta == "n":
            print("Enjuague omitido")
            return

        print("\nIniciando enjuague")

        SonidosLavadora.enjuague(self._tipo_lavadora)

        self._ultimo_sonido = "enjuague"

        time.sleep(2)

        print("Ropa enjuagada")

        print("\nIniciando centrifugado...")

        SonidosLavadora.centrifugado(self._tipo_lavadora)

        time.sleep(2)


    # SECADO
    def _secar(self):

        print("\nIniciando secado")

        SonidosLavadora.secado(self._tipo_lavadora)

        self._ultimo_sonido = "secado"

        time.sleep(3)

        print("Ropa seca")


    # CÁLCULO DE CONSUMO DE ENERGÍA
    def __calcular_consumo_energia(self):

        # Obtiene la tarifa según el estrato
        tarifa = self.TARIFAS_ESTRATO.get(self._estrato)

        # Fórmula de consumo
        kwh = self.POTENCIA_KW * (self._tiempo_lavado / 60)

        # Costo total de energía
        costo = kwh * tarifa

        return costo


    # REPORTE DEL CLIENTE
    """ def _mostrar_reporte_cliente(self, nombre):

        # Costo base del lavado
        kilos_totales = sum(k for _, k in self._lavados_cliente)
        costo_base = kilos_totales * self.PRECIO_KILO

        recargo = 0

        # Aplica recargo si la prenda es especial
        if self._tipo_ropa in self.PRENDAS_ESPECIALES:
            recargo = costo_base * self.AUMENTO_ESPECIAL

        subtotal = costo_base + recargo
        iva = subtotal * self.IVA
        total = subtotal + iva

        # Ganancia del negocio
        ganancia = costo_base * 0.30

        # Consumo de energía
        energia = self.__calcular_consumo_energia()

        # Fecha actual
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Tipo de lavadora
        metodo = "Inteligente" if self._tipo_lavadora == "inteligente" else "Estándar"

        print("\n" + "="*50)
        print("              REPORTE CLIENTE")
        print("="*50)

        print(f"Cliente           : {nombre}")
        print(f"Fecha             : {fecha}")
        print("Prendas lavadas:")

        for ropa, kilos in self._lavados_cliente:
            print(f" - {ropa} : {int(kilos)} kg")
        print(f"\nKilos totales     : {int(kilos_totales)} kg")
        print(f"Método de lavado  : {metodo}")

        print("-"*50)

        print(f"Costo por kilo    : ${self.PRECIO_KILO:,.2f}")
        print(f"Costo base        : ${costo_base:,.2f}")

        if recargo > 0:
            print(f"Recargo especial  : ${recargo:,.2f}")

        print(f"IVA (19%)         : ${iva:,.2f}")

        print("-"*50)

        print(f"TOTAL A PAGAR     : ${total:,.2f}")

        print("="*50)
        print("Gracias por usar Lava Smart")
        print("="*50)
        


        # Diccionario con datos para los reportes
        datos = {
            "cliente": nombre,
            "fecha": fecha,
            "kilos": self._kilos,
            "tipo_ropa": self._tipo_ropa,
            "metodo": metodo,
            "precio_kilo": self.PRECIO_KILO,
            "costo_base": round(costo_base, 2),
            "recargo": round(recargo, 2),
            "iva": round(iva, 2),
            "total": round(total, 2),
            "ganancia": round(ganancia, 2),
            "energia": round(energia, 2),
            "agua": self._kilos * 10
        }

        # Genera archivos de reporte
        Reportes.generar_factura_txt(datos)
        Reportes.generar_excel(datos)

        return datos
 """

    # CICLO COMPLETO DE LAVADO
    def ciclo_terminado(self, nombre):

        try:

            # Valida kilos
            self._validar_kilos()

            # Llenado de agua
            self._llenar()

            # Proceso de lavado (polimorfismo)
            continuar = self.lavar()

            if continuar is False:
                return None

            # Enjuague
            self._enjuagar()

            # Pregunta si desea secar
            secar = self._validar_sn(
                "¿Desea secar la ropa? (s/n): "
            )

            if secar == "s":
                self._secar()

            # Sonido final
            SonidosLavadora.fin(self._tipo_lavadora)
            
            self._lavados_cliente.append((self._tipo_ropa, self._kilos))
            return {
                "tipo_ropa": self._tipo_ropa,
                "kilos": self._kilos,
                "metodo": "Inteligente" if self._tipo_lavadora == "inteligente" else "Estándar"
            }

        # Manejo de interrupciones del usuario
        except (EOFError, KeyboardInterrupt):

            print("\nSistema detenido por el usuario")

        # Manejo de errores generales
        except Exception as e:

            SonidosLavadora.reproducir(self._tipo_lavadora, "error")

            print("Error en el ciclo:", e)