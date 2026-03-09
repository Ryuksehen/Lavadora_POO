# Librería de Windows que permite reproducir sonidos (.wav)
import winsound

# Librería que permite trabajar con rutas y carpetas del sistema
import os
# Esta clase se encarga de manejar y reproducir todos los sonidos
# que utiliza la lavadora durante el programa
class SonidosLavadora:

    # Carpeta principal donde están guardados los sonidos
    BASE_PATH = "Sonidos"

    @staticmethod
    def reproducir(tipo, sonido):
        """
        tipo = estandar / inteligente
        sonido = nombre del archivo
        """

        # Se arma la ruta completa del archivo de sonido
        # Ejemplo: Sonidos/inteligente/lavado.wav
        ruta = os.path.join(SonidosLavadora.BASE_PATH, tipo, f"{sonido}.wav")
        
        try:
            # Se reproduce el sonido usando la librería winsound
            winsound.PlaySound(ruta, winsound.SND_FILENAME)

        # Si el archivo no existe o ocurre un error se muestra el mensaje
        except Exception:
            print(f"No se encontró el sonido: {ruta}")


    # SONIDOS GENERALES
    # Cada uno de estos métodos llama a la función reproducir()
    # para evitar repetir código

    @staticmethod
    def encender(tipo):
        # Sonido cuando la lavadora se enciende
        SonidosLavadora.reproducir(tipo, "encender")

    @staticmethod
    def seleccionar_programa(tipo):
        # Sonido cuando el usuario selecciona el programa de lavado
        SonidosLavadora.reproducir(tipo, "seleccionPrograma")

    @staticmethod
    def llenado(tipo):
        # Sonido cuando el tanque se está llenando de agua
        SonidosLavadora.reproducir(tipo, "llenado")
        
    @staticmethod
    def inicioLavado(tipo):
        # Sonido cuando comienza el ciclo de lavado
        SonidosLavadora.reproducir(tipo, "inicioLavado")

    @staticmethod
    def lavado(tipo):
        # Sonido que representa el movimiento del tambor lavando
        SonidosLavadora.reproducir(tipo, "lavado")

    @staticmethod
    def enjuague(tipo):
        # Sonido del proceso de enjuague
        SonidosLavadora.reproducir(tipo, "enjuague")

    @staticmethod
    def drenado(tipo):
        # Sonido cuando el agua se está drenando del tanque
        SonidosLavadora.reproducir(tipo, "drenado")

    @staticmethod
    def centrifugado(tipo):
        # Sonido del centrifugado para sacar el agua de la ropa
        SonidosLavadora.reproducir(tipo, "centrifugado")

    @staticmethod
    def secado(tipo):
        # Sonido del proceso de secado
        SonidosLavadora.reproducir(tipo, "secado")

    @staticmethod
    def pausa(tipo):
        # Sonido cuando la lavadora entra en pausa
        SonidosLavadora.reproducir(tipo, "pausa")

    @staticmethod
    def reanudar(tipo):
        # Sonido cuando la lavadora continúa después de una pausa
        SonidosLavadora.reproducir(tipo, "reanudar")

    @staticmethod
    def fin(tipo):
        # Sonido que indica que el ciclo terminó
        SonidosLavadora.reproducir(tipo, "fin")
        
    @staticmethod
    def error(tipo):
        # Sonido que se reproduce si ocurre algún error
        SonidosLavadora.reproducir(tipo, "error")

    @staticmethod
    def wifi(tipo):
        # Sonido cuando la lavadora se conecta al WiFi
        SonidosLavadora.reproducir(tipo, "wifi")