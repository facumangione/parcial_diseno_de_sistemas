from python_forestacion.Entidades.terrenos.plantacion import Plantacion

class RegistroForestal:
    """Registro centralizado de todas las plantaciones."""

    def __init__(self):
        self._plantaciones: dict[str, Plantacion] = {}

    def agregar_plantacion(self, plantacion: Plantacion) -> None:
        self._plantaciones[plantacion.nombre] = plantacion

    def listar_todas(self) -> list[Plantacion]:
        return list(self._plantaciones.values())

    def buscar_plantacion(self, nombre: str) -> Plantacion | None:
        return self._plantaciones.get(nombre)

    def eliminar_plantacion(self, nombre: str) -> bool:
        if nombre in self._plantaciones:
            del self._plantaciones[nombre]
            return True
        return False
