class Observable:
    """Clase Observable genérica que mantiene una lista de observadores."""

    def __init__(self):
        self._observadores = []

    def agregar_observador(self, observador):
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador):
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar(self, *args, **kwargs):
        for observador in self._observadores:
            observador.actualizar(self, *args, **kwargs)
