import random
import time

class Sensor:
    def __init__(self):
        self.temperatura = 0
        self.humedad = 0
        self.ejecuta = True

    def leer_datos(self):
        while self.ejecuta:
            try:
                self.temperatura = random.uniform(0, 50)  # Temperatura entre 0 y 50 °C
                self.humedad = random.uniform(20, 90)     # Humedad entre 20% y 90%
                time.sleep(2)
            except Exception as e:
                print(f"Error en la generación de datos: {e}")
            finally:
                pass  # Aquí podrías liberar recursos si se necesitaran

    def detener(self):
        self.ejecuta = False
