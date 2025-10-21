import os
import pickle
from python_forestacion.excepciones.persistencia_exception import PersistenciaException

class Paquete:

    def __init__(self, ruta_base: str = "data"):
        self._ruta_base = ruta_base
        if not os.path.exists(self._ruta_base):
            os.makedirs(self._ruta_base)

    def guardar(self, objeto, nombre_archivo: str):
        ruta = os.path.join(self._ruta_base, f"{nombre_archivo}.dat")
        try:
            with open(ruta, "wb") as archivo:
                pickle.dump(objeto, archivo)
        except Exception as e:
            raise PersistenciaException(str(e))

    def cargar(self, nombre_archivo: str):
        ruta = os.path.join(self._ruta_base, f"{nombre_archivo}.dat")
        try:
            with open(ruta, "rb") as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            raise PersistenciaException(f"El archivo {nombre_archivo}.dat no existe.")
        except Exception as e:
            raise PersistenciaException(str(e))
