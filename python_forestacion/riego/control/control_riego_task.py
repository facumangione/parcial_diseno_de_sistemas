from python_forestacion.patrones.observer.observer import Observer
from constante import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO

class ControlRiegoTask(Observer):
    """Controlador que decide activar o no el riego según lecturas de sensores."""

    def __init__(self):
        self.temperatura = None
        self.humedad = None
        self.riego_activado = False

    def actualizar(self, observable, *args, **kwargs):
        if observable.tipo == "temperatura":
            self.temperatura = kwargs.get("valor")
        elif observable.tipo == "humedad":
            self.humedad = kwargs.get("valor")

        self._evaluar_riego()

    def _evaluar_riego(self):
        """Evalúa las condiciones y decide si activar el riego."""
        if self.temperatura is None or self.humedad is None:
            return

        if (TEMP_MIN_RIEGO <= self.temperatura <= TEMP_MAX_RIEGO) and self.humedad < HUMEDAD_MAX_RIEGO:
            self.riego_activado = True
        else:
            self.riego_activado = False

    def estado_riego(self) -> str:
        """Devuelve el estado actual del riego."""
        if self.riego_activado:
            return f"Riego ACTIVADO | Temp: {self.temperatura}°C | Humedad: {self.humedad}%"
        return f"Riego en reposo | Temp: {self.temperatura}°C | Humedad: {self.humedad}%"
