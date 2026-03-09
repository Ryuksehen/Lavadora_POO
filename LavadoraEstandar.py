from LavadoraBase import LavadoraBase
from SonidosLavadora import SonidosLavadora

# Librería que permite simular tiempo real con pausas
import time

class LavadoraEstandar(LavadoraBase):
    def __init__(self, kilos, tipo_ropa, estrato):

        super().__init__(kilos, tipo_ropa, estrato, "estandar")


    def lavar(self):

        # Indica el tipo de lavado
        print("\nModo de lavado: ESTÁNDAR")

        # Mensaje informativo del sistema
        print("Configuración manual del ciclo")

        # Reproduce el sonido del lavado
        SonidosLavadora.lavado(self._tipo_lavadora)

        # Guarda el último sonido ejecutado
        self._ultimo_sonido = "lavado"

        # Simula un pequeño tiempo antes de iniciar
        time.sleep(1)

        print("Iniciando lavado tradicional...")

        # Ejecuta la simulación del tambor (definida en la clase base)
        continuar = self._simular_tambor()

        # Si el usuario canceló el ciclo
        if not continuar:

            print("Lavado cancelado")

            return False

        # Mensaje final si el lavado termina correctamente
        print("Lavado estándar finalizado")

        return True