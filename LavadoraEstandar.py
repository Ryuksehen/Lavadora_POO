from LavadoraBase import LavadoraBase
from SonidosLavadora import SonidosLavadora
import time


class LavadoraEstandar(LavadoraBase):

    def __init__(self, kilos, tipo_ropa, estrato):

        super().__init__(kilos, tipo_ropa, estrato, "estandar")

    def lavar(self):

        print("\nModo de lavado: ESTÁNDAR")

        print("Configuración manual del ciclo")

        SonidosLavadora.lavado(self._tipo_lavadora)
        self._ultimo_sonido = "lavado"

        time.sleep(1)

        print("Iniciando lavado tradicional...")

        continuar = self._simular_tambor()

        if not continuar:

            print("Lavado cancelado")
            return False

        print("Lavado estándar finalizado")

        return True