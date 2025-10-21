class Herramienta:
    """Representa una herramienta de trabajo."""

    def __init__(self, nombre: str, estado: str):
        self.nombre = nombre
        self.estado = estado

    def usar(self) -> None:
        self.estado = "en uso"

    def reparar(self) -> None:
        self.estado = "operativa"
