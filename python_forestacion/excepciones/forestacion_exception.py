class ForestacionException(Exception):
    """
    Excepción base para todas las excepciones del sistema.
    Permite mantener una jerarquía común y un punto central de captura.
    """

    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"[PythonForestal] {self.mensaje}"
