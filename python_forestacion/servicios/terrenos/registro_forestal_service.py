from python_forestacion.Entidades.terrenos.registro_forestal import RegistroForestal

class RegistroForestalService:
    """Servicio que maneja el registro general de plantaciones."""

    def __init__(self, registro: RegistroForestal):
        self._registro = registro

    def agregar_plantacion(self, plantacion):
        self._registro.agregar_plantacion(plantacion)

    def listar_todas(self):
        return self._registro.listar_todas()

    def buscar_plantacion(self, nombre: str):
        return self._registro.buscar_plantacion(nombre)

    def eliminar_plantacion(self, nombre: str) -> bool:
        return self._registro.eliminar_plantacion(nombre)
