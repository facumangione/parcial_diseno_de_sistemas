from arbol import Arbol

class Pino(Arbol):
    """Cultivo tipo Pino."""

    def __init__(self, superficie: float, altura: float):
        super().__init__("Pino", superficie, altura)

    def absorber_agua(self, cantidad: float) -> None:
        if cantidad < 10:
            raise ValueError("El pino requiere al menos 10 L de agua para absorber correctamente.")
        self.altura += 0.05
