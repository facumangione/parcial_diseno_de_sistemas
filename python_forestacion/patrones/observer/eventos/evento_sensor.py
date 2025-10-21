from python_forestacion.patrones.observer.observable import Observable

class EventoSensor(Observable):
    """Evento observable que notifica cambios en sensores ambientales."""

    def __init__(self, tipo: str):
        super().__init__()
        self.tipo = tipo
        self.valor = 0

    def actualizar_valor(self, nuevo_valor: float):
        self.valor = nuevo_valor
        self.notificar(valor=nuevo_valor)
