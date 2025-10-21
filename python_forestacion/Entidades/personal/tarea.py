from datetime import date
from herramienta import Herramienta

class Tarea:
    """Actividad asignada a un trabajador."""

    def __init__(self, descripcion: str, fecha: date, herramienta: Herramienta):
        self.descripcion = descripcion
        self.fecha = fecha
        self.herramienta = herramienta
        self.completada = False

    def completar(self) -> None:
        self.completada = True
