
"""
PythonForestal - Sistema de Gestión Forestal
============================================

Sistema educativo que demuestra la implementación de patrones de diseño
en Python con enfoque en gestión forestal y agrícola.

Patrones implementados:
- SINGLETON: CultivoServiceRegistry
- FACTORY METHOD: CultivoFactory
- OBSERVER: Sistema de sensores y eventos
- STRATEGY: Algoritmos de absorción de agua
- REGISTRY: Dispatch polimórfico

Versión: 1.0.0
Python: 3.13+
Autor: PythonForestal Contributors
"""

__version__ = "1.0.0"
__author__ = "PythonForestal Contributors"
__all__ = [
    # Servicios principales
    'FincasService',
    'PlantacionService',
    'TierraService',
    'TrabajadorService',
    
    # Patrones
    'CultivoFactory',
    'CultivoServiceRegistry',
    
    # Entidades principales
    'Tierra',
    'Plantacion',
    'RegistroForestal',
    'Trabajador',
    
    # Excepciones
    'ForestacionException',
    'AguaAgotadaException',
    'SuperficieInsuficienteException',
    'PersistenciaException',
]

# Importaciones principales para facilitar el uso del paquete
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

from python_forestacion.Entidades.terrenos.tierra import Tierra
from python_forestacion.Entidades.terrenos.plantacion import Plantacion
from python_forestacion.Entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.Entidades.personal.trabajador import Trabajador

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException