import tkinter as tk
import threading
from Sensor import Sensor
from Interfaz import Interfaz

class Monitor:
    def __init__(self):
        self.sensor = Sensor()
        self.root = None
        self.app = None

    def iniciar_ventana(self):
        self.root = tk.Tk()
        return self.root

    def iniciar_sensores(self):
        hilo_sensor = threading.Thread(target=self.sensor.leer_datos, daemon=True)
        hilo_sensor.start()

    def iniciar_interfaz(self):
        self.app = Interfaz(self.root, self.sensor)


monitor = Monitor()
ventana = monitor.iniciar_ventana()
monitor.iniciar_sensores()
monitor.iniciar_interfaz()

ventana.mainloop()
monitor.sensor.detener()

