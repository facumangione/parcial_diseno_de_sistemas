from datetime import datetime
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción estacional: varía según la época del año.
    """

    def absorber(self, cantidad: float) -> float:
        mes = datetime.now().month
        if mes in (12, 1, 2):  # verano
            return cantidad * 1.1
        elif mes in (6, 7, 8):  # invierno
            return cantidad * 0.9
        return cantidad
