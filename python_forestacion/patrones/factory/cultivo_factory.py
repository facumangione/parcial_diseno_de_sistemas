from python_forestacion.Entidades.cultivos.pino import Pino
from python_forestacion.Entidades.cultivos.olivo import Olivo
from python_forestacion.Entidades.cultivos.lechuga import Lechuga
from python_forestacion.Entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.Entidades.cultivos.tipo_aceituna import TipoAceituna

class CultivoFactory:
    """
    Fábrica de cultivos.
    Permite crear instancias dinámicamente según el tipo especificado.
    """

    @staticmethod
    def crear_cultivo(tipo: str, **kwargs):
        tipo = tipo.lower()
        if tipo == "pino":
            return Pino(kwargs.get("superficie", 10), kwargs.get("altura", 1.0))
        elif tipo == "olivo":
            tipo_aceituna = kwargs.get("tipo_aceituna", TipoAceituna.MANZANILLA)
            return Olivo(kwargs.get("superficie", 8), kwargs.get("altura", 1.2), tipo_aceituna)
        elif tipo == "lechuga":
            return Lechuga(kwargs.get("superficie", 2), kwargs.get("dias_crecimiento", 60))
        elif tipo == "zanahoria":
            return Zanahoria(kwargs.get("superficie", 3), kwargs.get("dias_crecimiento", 80), kwargs.get("profundidad", 0.3))
        else:
            raise ValueError(f"Tipo de cultivo no reconocido: {tipo}")
