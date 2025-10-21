from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """Estrategia de absorción constante: se mantiene igual en el tiempo."""

    def absorber(self, cantidad: float) -> float:
        return cantidad * 0.8
