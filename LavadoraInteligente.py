from LavadoraBase import LavadoraBase
from SonidosLavadora import SonidosLavadora
import time

class LavadoraInteligente(LavadoraBase):
    def __init__(self, kilos, tipo_ropa, estrato):
        super().__init__(kilos, tipo_ropa, estrato, "inteligente")
        
        # Indica si la lavadora está conectada a WiFi
        self._wifi = False

        # Indica que la lavadora tiene sensores inteligentes
        self._sensores = True
 

    # DETECCIÓN AUTOMÁTICA DE ROPA
    def detectar_tipo_ropa(self):

        print("\nSensores analizando tipo de ropa...")

        # Simula el análisis de sensores
        time.sleep(2)

        # Dependiendo del tipo de ropa
        # se configura un modo de lavado diferente

        if self._tipo_ropa == "interior":

            print("Modo delicado activado")

            # Reduce el tiempo para proteger telas delicadas
            self._tiempo_lavado = 15

        elif self._tipo_ropa == "pijamas":

            print("Modo suave activado")

            self._tiempo_lavado = 18

        elif self._tipo_ropa == "vestidos":

            print("Modo protección de telas activado")

            self._tiempo_lavado = 16

        else:

            # Modo automático estándar
            print("Modo inteligente estándar")

            self._tiempo_lavado = 20


    # CONEXIÓN WIFI
    def conectar_wifi(self):

        print("\nConexión remota de la lavadora")

        while True:

            try:

                # Solicita nombre de la red WiFi
                red = input("Ingrese nombre de red WiFi: ").strip()

                if red == "":
                    print("Nombre de red inválido")
                    continue

                # Solicita contraseña
                password = input("Ingrese contraseña WiFi: ").strip()

                # Validación básica de contraseña
                if len(password) < 4:
                    print("Contraseña demasiado corta")
                    continue

                # Marca la lavadora como conectada
                self._wifi = True

                print("\nLavadora conectada a la red:", red)

                # Sonido de conexión WiFi
                SonidosLavadora.reproducir(self._tipo_lavadora, "wifi")

                print("Ahora puede controlar la lavadora desde su dispositivo")

                return

            except (EOFError, KeyboardInterrupt):

                # Si el usuario cancela la conexión
                print("\nConexión WiFi cancelada")

                return

    # OPCIONES DE LAVADO INTELIGENTE
    def mostrar_opciones_lavado(self):

        print("\nOpciones inteligentes disponibles")

        # Sonido de selección de programa
        SonidosLavadora.seleccionar_programa(self._tipo_lavadora)

        print("1. Lavado ecológico")
        print("2. Lavado profundo")
        print("3. Lavado rápido")
        print("4. Lavado automático por sensores")

        while True:

            try:

                opcion = input("Seleccione una opción: ")

                if opcion == "1":

                    print("Modo ecológico activado")

                    # Mayor tiempo pero menor consumo
                    self._tiempo_lavado = 25

                    return

                elif opcion == "2":

                    print("Modo profundo activado")

                    # Lavado más largo para ropa muy sucia
                    self._tiempo_lavado = 30

                    return

                elif opcion == "3":

                    print("Modo rápido activado")

                    # Lavado corto
                    self._tiempo_lavado = 10

                    return

                elif opcion == "4":

                    # Activación del sistema de sensores
                    self.detectar_tipo_ropa()

                    return

                else:

                    print("Opción inválida")

            except (EOFError, KeyboardInterrupt):

                print("\nSelección cancelada")

                return


    # LAVADO INTELIGENTE (
    def lavar(self):

        print("\nModo de lavado: INTELIGENTE")

        # Si no está conectada a WiFi se solicita conexión
        if not self._wifi:
            self.conectar_wifi()

        # Muestra los modos de lavado inteligente
        self.mostrar_opciones_lavado()

        print("\nIniciando ciclo inteligente optimizado...")

        # Ejecuta la simulación del tambor
        continuar = self._simular_tambor()

        # Si el usuario cancela el lavado
        if not continuar:
            
            SonidosLavadora.reproducir(self._tipo_lavadora, "error")

            print("Lavado cancelado por el usuario")

            return False

        print("Lavado inteligente finalizado")

        return True