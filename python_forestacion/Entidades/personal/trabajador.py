class Trabajador:
    """Representa un trabajador agrícola."""

    def __init__(self, nombre: str, dni: str, edad: int):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.apto_medico = None
        self.tareas = []

    def asignar_tarea(self, tarea) -> None:
        self.tareas.append(tarea)

    def asignar_apto_medico(self, apto) -> None:
        self.apto_medico = apto
