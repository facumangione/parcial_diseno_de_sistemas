from python_forestacion.patrones.observer.observable import Observable

class EventoPlantacion(Observable):
    """Evento observable asociado a acciones dentro de una plantación."""

    def __init__(self, nombre: str):
        super().__init__()
        self.nombre = nombre

    def registrar_evento(self, mensaje: str):
        self.notificar(mensaje=mensaje)
