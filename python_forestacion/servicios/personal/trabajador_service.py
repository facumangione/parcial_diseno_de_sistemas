from python_forestacion.Entidades.personal.trabajador import Trabajador

class TrabajadorService:
    """Servicio para gestionar los trabajadores."""

    def __init__(self):
        self._trabajadores: dict[str, Trabajador] = {}

    def registrar_trabajador(self, trabajador: Trabajador):
        self._trabajadores[trabajador.dni] = trabajador

    def listar_trabajadores(self) -> list[Trabajador]:
        return list(self._trabajadores.values())

    def buscar_trabajador(self, dni: str) -> Trabajador | None:
        return self._trabajadores.get(dni)
