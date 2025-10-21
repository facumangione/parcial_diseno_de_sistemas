import random
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

class TemperaturaReaderTask(EventoSensor):
    """Simula un sensor de temperatura ambiente."""

    def __init__(self):
        super().__init__("temperatura")

    def leer_temperatura(self):
        """Genera una lectura aleatoria y notifica a los observadores."""
        valor = round(random.uniform(5, 40), 2)
        self.actualizar_valor(valor)
        return valor
