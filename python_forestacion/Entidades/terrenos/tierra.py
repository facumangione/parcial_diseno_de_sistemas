from Entidades.terrenos.plantacion import Plantacion

class Tierra:
    """Representa un terreno agrícola."""

    def __init__(self, id_padron: int, superficie: float, domicilio: str, nombre_plantacion: str):
        self.id_padron = id_padron
        self.superficie = superficie
        self.domicilio = domicilio
        self.nombre_plantacion = nombre_plantacion
        self.plantacion: Plantacion | None = None

    def set_plantacion(self, plantacion: Plantacion) -> None:
        self.plantacion = plantacion


    def __str__(self) -> str:
        return f"Tierra {self.id_padron} ({self.superficie} m², {self.domicilio})"
