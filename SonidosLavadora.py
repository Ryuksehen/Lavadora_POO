import winsound
import os


class SonidosLavadora:

    BASE_PATH = "Sonidos"

    @staticmethod
    def reproducir(tipo, sonido):
        """
        tipo = estandar / inteligente
        sonido = nombre del archivo
        """

        ruta = os.path.join(SonidosLavadora.BASE_PATH, tipo, f"{sonido}.wav")

        try:
            winsound.PlaySound(ruta, winsound.SND_FILENAME)
        except:
            print(f"⚠️ No se encontró el sonido: {ruta}")


    # SONIDOS GENERALES

    @staticmethod
    def encender(tipo):
        SonidosLavadora.reproducir(tipo, "encender")

    @staticmethod
    def seleccionar_programa(tipo):
        SonidosLavadora.reproducir(tipo, "seleccionPrograma")

    @staticmethod
    def llenado(tipo):
        SonidosLavadora.reproducir(tipo, "llenado")

    @staticmethod
    def lavado(tipo):
        SonidosLavadora.reproducir(tipo, "lavado")

    @staticmethod
    def enjuague(tipo):
        SonidosLavadora.reproducir(tipo, "enjuague")

    @staticmethod
    def drenado(tipo):
        SonidosLavadora.reproducir(tipo, "drenado")

    @staticmethod
    def centrifugado(tipo):
        SonidosLavadora.reproducir(tipo, "centrifugado")

    @staticmethod
    def secado(tipo):
        SonidosLavadora.reproducir(tipo, "secado")

    @staticmethod
    def pausa(tipo):
        SonidosLavadora.reproducir(tipo, "pausa")

    @staticmethod
    def reanudar(tipo):
        SonidosLavadora.reproducir(tipo, "reanudar")

    @staticmethod
    def fin(tipo):
        SonidosLavadora.reproducir(tipo, "fin")