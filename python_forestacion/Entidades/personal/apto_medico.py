from datetime import date

class AptoMedico:
    """Certificación médica del trabajador."""

    def __init__(self, fecha_emision: date, valido_hasta: date, observaciones: str):
        self.fecha_emision = fecha_emision
        self.valido_hasta = valido_hasta
        self.observaciones = observaciones

    def esta_vigente(self) -> bool:
        return date.today() <= self.valido_hasta
