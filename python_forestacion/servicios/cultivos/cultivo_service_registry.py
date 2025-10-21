from python_forestacion.patrones.singleton.singleton import singleton
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

# Importar tipos de cultivos para el registro
from python_forestacion.Entidades.cultivos.pino import Pino
from python_forestacion.Entidades.cultivos.olivo import Olivo
from python_forestacion.Entidades.cultivos.lechuga import Lechuga
from python_forestacion.Entidades.cultivos.zanahoria import Zanahoria

@singleton
class CultivoServiceRegistry:

    def __init__(self):
        self._servicios: dict[str, CultivoService] = {}
        
        # Diccionarios de handlers por tipo (patrón Registry)
        self._mostrar_datos_handlers = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    def registrar_servicio(self, nombre: str, servicio: CultivoService):
        self._servicios[nombre] = servicio

    def obtener_servicio(self, nombre: str) -> CultivoService | None:
        return self._servicios.get(nombre)

    def listar_servicios(self) -> list[str]:
        return list(self._servicios.keys())
    
    def mostrar_datos(self, cultivo):
        tipo = type(cultivo)
        
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo.__name__}")
        
        # Dispatch automático al handler correcto
        return self._mostrar_datos_handlers[tipo](cultivo)
    
    # ========================================================================
    # HANDLERS ESPECÍFICOS POR TIPO (patrón Registry)
    # ========================================================================
    
    def _mostrar_datos_pino(self, cultivo: Pino):
        print(f"     Tipo: Pino")
        print(f"     Superficie: {cultivo.superficie} m2")
        print(f"     Altura: {cultivo.altura} m")
        if hasattr(cultivo, 'dias_crecimiento'):
            print(f"     Dias de crecimiento: {cultivo.dias_crecimiento}")
    
    def _mostrar_datos_olivo(self, cultivo: Olivo):
        print(f"     Tipo: Olivo")
        print(f"     Superficie: {cultivo.superficie} m2")
        print(f"     Altura: {cultivo.altura} m")
        print(f"     Tipo de aceituna: {cultivo.tipo_aceituna.value}")
        print(f"     Produccion anual: {cultivo.produccion_anual}")
    
    def _mostrar_datos_lechuga(self, cultivo: Lechuga):
        print(f"     Tipo: Lechuga")
        print(f"     Superficie: {cultivo.superficie} m2")
        print(f"     Dias de crecimiento: {cultivo.dias_crecimiento}")
        print(f"     Regada: {cultivo.regada}")
    
    def _mostrar_datos_zanahoria(self, cultivo: Zanahoria):
        print(f"     Tipo: Zanahoria")
        print(f"     Superficie: {cultivo.superficie} m2")
        print(f"     Dias de crecimiento: {cultivo.dias_crecimiento}")
        print(f"     Profundidad: {cultivo.profundidad} m")
        print(f"     Regada: {cultivo.regada}")