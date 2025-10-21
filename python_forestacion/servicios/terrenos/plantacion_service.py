from python_forestacion.Entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

class PlantacionService:
    """Servicio para manejar las operaciones sobre plantaciones."""

    def __init__(self):
        self._plantaciones: dict[str, Plantacion] = {}

    def registrar_plantacion(self, plantacion: Plantacion):
        if plantacion.superficie <= 0:
            raise SuperficieInsuficienteException()
        self._plantaciones[plantacion.nombre] = plantacion

    def regar(self, nombre: str, cantidad: float):
        plantacion = self._plantaciones.get(nombre)
        if not plantacion:
            raise ValueError("Plantación no encontrada.")
        if cantidad > plantacion.agua_disponible:
            raise AguaAgotadaException()
        plantacion.regar_todos(cantidad)

    def listar_plantaciones(self) -> list[Plantacion]:
        return list(self._plantaciones.values())
