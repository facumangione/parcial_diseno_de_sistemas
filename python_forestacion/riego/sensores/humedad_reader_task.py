import random
from python_forestacion.patrones.observer.eventos.evento_sensor import EventoSensor

class HumedadReaderTask(EventoSensor):
    """Simula un sensor de humedad del suelo."""

    def __init__(self):
        super().__init__("humedad")

    def leer_humedad(self):
        """Genera una lectura aleatoria y notifica a los observadores."""
        valor = round(random.uniform(10, 80), 2)
        self.actualizar_valor(valor)
        return valor
