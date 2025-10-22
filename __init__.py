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
"""

__version__ = "1.0.0"
__author__ = "PythonForestal Contributors"

# Importaciones principales para facilitar el uso del paquete
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

__all__ = [
    'FincasService',
    'PlantacionService',
    'CultivoFactory',
]