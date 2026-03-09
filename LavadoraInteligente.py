from LavadoraBase import LavadoraBase
from SonidosLavadora import SonidosLavadora
import time


class LavadoraInteligente(LavadoraBase):

    
    # Constructor
    
    def __init__(self, kilos, tipo_ropa, estrato):

        super().__init__(kilos, tipo_ropa, estrato, "inteligente")

        self._wifi = False
        self._sensores = True
 
    
    # Detección automática de ropa
    
    def detectar_tipo_ropa(self):

        print("\nSensores analizando tipo de ropa...")

        time.sleep(2)

        if self._tipo_ropa == "interior":

            print("Modo delicado activado")
            self._tiempo_lavado = 15

        elif self._tipo_ropa == "pijamas":

            print("Modo suave activado")
            self._tiempo_lavado = 18

        elif self._tipo_ropa == "vestidos":

            print("Modo protección de telas activado")
            self._tiempo_lavado = 16

        else:

            print("Modo inteligente estándar")
            self._tiempo_lavado = 20

    # Conexión WiFi
    def conectar_wifi(self):

        print("\nConexión remota de la lavadora")

        while True:

            try:

                red = input("Ingrese nombre de red WiFi: ").strip()

                if red == "":
                    print("Nombre de red inválido")
                    continue

                password = input("Ingrese contraseña WiFi: ").strip()

                if len(password) < 4:
                    print("Contraseña demasiado corta")
                    continue

                self._wifi = True

                print("\nLavadora conectada a la red:", red)

                SonidosLavadora.reproducir(self._tipo_lavadora, "wifi")

                print("Ahora puede controlar la lavadora desde su dispositivo")

                return

            except (EOFError, KeyboardInterrupt):

                print("\nConexión WiFi cancelada")
                return

    # Opciones de lavado inteligente
    
    def mostrar_opciones_lavado(self):

        print("\nOpciones inteligentes disponibles")
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
                    self._tiempo_lavado = 25
                    return

                elif opcion == "2":

                    print("Modo profundo activado")
                    self._tiempo_lavado = 30
                    return

                elif opcion == "3":

                    print("Modo rápido activado")
                    self._tiempo_lavado = 10
                    return

                elif opcion == "4":

                    self.detectar_tipo_ropa()
                    return

                else:

                    print("Opción inválida")

            except (EOFError, KeyboardInterrupt):

                print("\nSelección cancelada")
                return

    
    # Lavado inteligente
    
    def lavar(self):

        print("\nModo de lavado: INTELIGENTE")

        if not self._wifi:
            self.conectar_wifi()

        self.mostrar_opciones_lavado()


        print("\nIniciando ciclo inteligente optimizado...")
        

        continuar = self._simular_tambor()

        if not continuar:
            
            SonidosLavadora.reproducir(self._tipo_lavadora, "error")

            print("Lavado cancelado por el usuario")
            return False

        print("Lavado inteligente finalizado")

        return True