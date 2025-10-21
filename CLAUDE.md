# Guía Técnica para Claude Code - PythonForestal

**Versión**: 1.0.0  
**Fecha**: Octubre 2025  
**Python**: 3.13+

---

## Tabla de Contenidos

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Convenciones de Código](#convenciones-de-código)
4. [Patrones de Diseño](#patrones-de-diseño)
5. [Guía de Desarrollo](#guía-de-desarrollo)
6. [Testing](#testing)
7. [Troubleshooting](#troubleshooting)
8. [Comandos Útiles](#comandos-útiles)

---

## Resumen Ejecutivo

### ¿Qué es PythonForestal?

Sistema educativo de gestión forestal que demuestra la implementación de **5 patrones de diseño** en Python:

1. **SINGLETON** - CultivoServiceRegistry
2. **FACTORY METHOD** - CultivoFactory
3. **OBSERVER** - Sistema de sensores y eventos
4. **STRATEGY** - Algoritmos de absorción de agua
5. **REGISTRY** - Dispatch polimórfico sin isinstance()

### Características Principales

- ✅ Gestión de 4 tipos de cultivos (Pino, Olivo, Lechuga, Zanahoria)
- ✅ Sistema de riego automatizado con sensores
- ✅ Gestión de personal con apto médico
- ✅ Persistencia con Pickle
- ✅ 28 tests unitarios (~93% cobertura)
- ✅ PEP 8 compliance 100%
- ✅ Solo biblioteca estándar (sin dependencias externas)

---

## Arquitectura del Sistema

### Estructura de Capas

```
┌─────────────────────────────────────┐
│      PRESENTACIÓN (main.py)         │
│   Demostración de patrones CLI      │
└─────────────────────────────────────┘
                 ▼
┌─────────────────────────────────────┐
│    SERVICIOS DE NEGOCIO             │
│  FincasService, Paquete             │
└─────────────────────────────────────┘
                 ▼
┌─────────────────────────────────────┐
│    SERVICIOS DE DOMINIO             │
│  PlantacionService, TierraService   │
└─────────────────────────────────────┘
                 ▼
┌─────────────────────────────────────┐
│         ENTIDADES (DTOs)            │
│  Cultivo, Tierra, Trabajador        │
└─────────────────────────────────────┘
                 ▼
┌─────────────────────────────────────┐
│    PATRONES / UTILIDADES            │
│  Factory, Strategy, Observer        │
└─────────────────────────────────────┘
```

### Paquetes Principales

```
python_forestacion/
├── Entidades/          # Objetos de dominio (DTOs)
│   ├── cultivos/       # Pino, Olivo, Lechuga, Zanahoria
│   ├── terrenos/       # Tierra, Plantacion, RegistroForestal
│   └── personal/       # Trabajador, Tarea, Herramienta
│
├── servicios/          # Lógica de negocio
│   ├── cultivos/       # Servicios por tipo de cultivo
│   ├── terrenos/       # Servicios de gestión territorial
│   ├── personal/       # Servicios de RRHH
│   └── negocio/        # Orquestación de alto nivel
│
├── patrones/           # Implementaciones de patrones
│   ├── singleton/      # Decorador Singleton
│   ├── factory/        # CultivoFactory
│   ├── observer/       # Observable[T] y Observer[T]
│   └── strategy/       # AbsorcionAguaStrategy + impls
│
├── riego/              # Sistema de riego automatizado
│   ├── sensores/       # TemperaturaReaderTask, HumedadReaderTask
│   └── control/        # ControlRiegoTask
│
├── excepciones/        # Excepciones de dominio
│   ├── ForestacionException (base)
│   ├── AguaAgotadaException
│   ├── SuperficieInsuficienteException
│   └── PersistenciaException
│
└── tests/              # Tests unitarios
    ├── test_excepciones.py
    ├── test_fincas_service.py
    └── test_riego.py
```

---

## Convenciones de Código

### 1. Nomenclatura (PEP 8)

```python
# Variables y funciones: snake_case
agua_disponible = 100
def calcular_absorcion(cantidad: float) -> int:
    pass

# Clases: PascalCase
class CultivoFactory:
    pass

# Constantes: UPPER_SNAKE_CASE (en constante.py)
AGUA_INICIAL_PLANTACION = 500.0
TEMP_MIN_RIEGO = 8

# Privados: prefijo _
class MiClase:
    def __init__(self):
        self._atributo_privado = 10
```

### 2. Type Hints OBLIGATORIOS

```python
# ✅ CORRECTO
def regar(self, cantidad: float) -> None:
    pass

def obtener_cultivos(self) -> list[Cultivo]:
    return self._cultivos

# ❌ INCORRECTO
def regar(self, cantidad):  # Sin type hints
    pass
```

### 3. Docstrings (Google Style)

```python
def plantar(self, plantacion: Plantacion, tipo: str, cantidad: int) -> None:
    """
    Planta cultivos del tipo especificado en la plantación.
    
    Args:
        plantacion: Plantación donde plantar
        tipo: Tipo de cultivo (Pino, Olivo, Lechuga, Zanahoria)
        cantidad: Número de cultivos a plantar
    
    Raises:
        SuperficieInsuficienteException: Si no hay espacio suficiente
        ValueError: Si el tipo de cultivo es desconocido
    
    Example:
        >>> service.plantar(mi_plantacion, "Pino", 5)
    """
    pass
```

### 4. Imports (Organización PEP 8)

```python
# Standard library
import os
import sys
from datetime import date, datetime
from typing import TYPE_CHECKING, List, Optional

# Third-party (si hubiera)
# import numpy as np

# Local application
from python_forestacion.Entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

# TYPE_CHECKING para evitar imports circulares
if TYPE_CHECKING:
    from python_forestacion.Entidades.terrenos.plantacion import Plantacion
```

### 5. Reglas Estrictas

#### ❌ NO PERMITIDO:

```python
# NO emojis (problemas de encoding en Windows)
print("🌲 Iniciando...")  # ❌

# NO lambdas
cultivos.sort(key=lambda c: c.nombre)  # ❌

# NO magic numbers
if cantidad > 10:  # ❌ ¿Qué significa 10?
    pass

# NO isinstance() en cascadas
if isinstance(cultivo, Pino):  # ❌ Usar Registry
    # ...
elif isinstance(cultivo, Olivo):
    # ...
```

#### ✅ PERMITIDO:

```python
# Solo ASCII
print("[OK] Iniciando...")  # ✅

# Métodos/funciones nombrados
def _obtener_nombre(cultivo):
    return cultivo.nombre
cultivos.sort(key=_obtener_nombre)  # ✅

# Constantes centralizadas
from constante import AGUA_MINIMA_RIEGO
if cantidad > AGUA_MINIMA_RIEGO:  # ✅
    pass

# Registry para dispatch
registry.mostrar_datos(cultivo)  # ✅
```

---

## Patrones de Diseño

### 1. SINGLETON

**Ubicación**: `servicios/cultivos/cultivo_service_registry.py`

**Implementación**:
```python
from python_forestacion.patrones.singleton.singleton import singleton

@singleton
class CultivoServiceRegistry:
    def __init__(self):
        self._servicios = {}
```

**Uso**:
```python
registry1 = CultivoServiceRegistry()
registry2 = CultivoServiceRegistry()
assert registry1 is registry2  # True - misma instancia
```

**Características**:
- Thread-safe con Lock
- Lazy initialization
- Decorador reutilizable

---

### 2. FACTORY METHOD

**Ubicación**: `patrones/factory/cultivo_factory.py`

**Implementación**:
```python
class CultivoFactory:
    @staticmethod
    def crear_cultivo(tipo: str, **kwargs) -> Cultivo:
        factories = {
            "pino": CultivoFactory._crear_pino,
            "olivo": CultivoFactory._crear_olivo,
            # ...
        }
        return factories[tipo.lower()]()
```

**Uso**:
```python
# Cliente NO conoce clases concretas
cultivo = CultivoFactory.crear_cultivo("Pino")
# Retorna tipo base Cultivo, no Pino concreto
```

**Ventajas**:
- Desacoplamiento
- Extensibilidad (agregar tipos sin modificar factory)
- Validación centralizada

---

### 3. OBSERVER

**Ubicación**: `patrones/observer/`

**Implementación**:
```python
from typing import Generic, TypeVar

T = TypeVar('T')

class Observable(Generic[T]):
    def __init__(self):
        self._observadores: list[Observer[T]] = []
    
    def notificar_observadores(self, evento: T) -> None:
        for obs in self._observadores:
            obs.actualizar(evento)
```

**Uso**:
```python
# Sensor es Observable[float]
sensor = TemperaturaReaderTask()

# Controlador es Observer[float]
controlador = ControlRiegoTask()

# Suscripción
sensor.agregar_observador(controlador)

# Notificación automática
sensor.leer_temperatura()  # Notifica a controlador
```

**Ventajas**:
- Tipo-seguro con Generics
- Desacoplamiento total
- Push-based (no polling)

---

### 4. STRATEGY

**Ubicación**: `patrones/strategy/`

**Implementación**:
```python
class AbsorcionAguaStrategy(ABC):
    @abstractmethod
    def calcular_absorcion(self, ...) -> int:
        pass

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    def calcular_absorcion(self, fecha, ...) -> int:
        if es_verano(fecha):
            return 5  # 5L en verano
        return 2      # 2L en invierno
```

**Uso**:
```python
# Inyección de estrategia
class PinoService(ArbolService):
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())

# Delegación a estrategia
agua = self._estrategia.calcular_absorcion(...)
```

**Ventajas**:
- Algoritmos intercambiables
- Sin modificar código cliente
- Testeable independientemente

---

### 5. REGISTRY (Bonus)

**Ubicación**: `servicios/cultivos/cultivo_service_registry.py`

**Implementación**:
```python
class CultivoServiceRegistry:
    def __init__(self):
        self._handlers = {
            Pino: self._mostrar_pino,
            Olivo: self._mostrar_olivo,
            # ...
        }
    
    def mostrar_datos(self, cultivo: Cultivo):
        tipo = type(cultivo)
        return self._handlers[tipo](cultivo)
```

**Ventajas**:
- Elimina isinstance() cascades
- O(1) lookup
- Fácil agregar tipos

---

## Guía de Desarrollo

### Setup Inicial

```bash
# 1. Clonar repositorio
git clone <repo-url>
cd parcial_diseno_de_sistemas

# 2. Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 3. Verificar versión de Python
python --version  # Debe ser 3.13+

# 4. Ejecutar sistema
python3 main.py

# 5. Ejecutar tests
python3 -m unittest discover -s python_forestacion/tests -t .
```

### Agregar Nuevo Tipo de Cultivo

**Paso 1**: Crear entidad en `Entidades/cultivos/`:
```python
# tomate.py
from python_forestacion.Entidades.cultivos.hortaliza import Hortaliza

class Tomate(Hortaliza):
    def __init__(self, superficie: float, dias_crecimiento: int):
        super().__init__("Tomate", superficie, dias_crecimiento)
    
    def absorber_agua(self, cantidad: float) -> None:
        if cantidad < 1.5:
            raise ValueError("El tomate necesita al menos 1.5L")
        self.regar()
```

**Paso 2**: Crear servicio en `servicios/cultivos/`:
```python
# tomate_service.py
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.Entidades.cultivos.tomate import Tomate

class TomateService(CultivoService):
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))
```

**Paso 3**: Registrar en Factory:
```python
# cultivo_factory.py
@staticmethod
def _crear_tomate() -> Tomate:
    return Tomate(superficie=0.25, dias_crecimiento=90)

@staticmethod
def crear_cultivo(tipo: str) -> Cultivo:
    factories = {
        # ... existentes
        "tomate": CultivoFactory._crear_tomate
    }
```

**Paso 4**: Registrar en Registry:
```python
# cultivo_service_registry.py
def __init__(self):
    self._mostrar_datos_handlers = {
        # ... existentes
        Tomate: self._mostrar_datos_tomate
    }

def _mostrar_datos_tomate(self, cultivo: Tomate):
    print(f"     Tipo: Tomate")
    # ...
```

**Paso 5**: Agregar constantes:
```python
# constante.py
SUPERFICIE_TOMATE = 0.25
AGUA_INICIAL_TOMATE = 2.0
```

---

## Testing

### Ejecutar Tests

```bash
# Todos los tests
python3 -m unittest discover -s python_forestacion/tests -t .

# Test específico
python3 -m unittest python_forestacion.tests.test_excepciones

# Con verbose
python3 -m unittest discover -s python_forestacion/tests -t . -v
```

### Estructura de Test

```python
import unittest

class TestMiComponente(unittest.TestCase):
    def setUp(self):
        """Ejecutado ANTES de cada test."""
        self.componente = MiComponente()
    
    def tearDown(self):
        """Ejecutado DESPUÉS de cada test."""
        # Limpieza
        pass
    
    def test_comportamiento_esperado(self):
        """Descripción del test."""
        resultado = self.componente.hacer_algo()
        self.assertEqual(resultado, valor_esperado)
```

### Coverage (Opcional)

```bash
# Instalar pytest-cov
pip install pytest-cov

# Ejecutar con coverage
pytest --cov=python_forestacion --cov-report=html

# Ver reporte
open htmlcov/index.html
```

---

## Troubleshooting

### Error: ModuleNotFoundError

```python
# ❌ Error común
from cultivo import Cultivo
# ModuleNotFoundError: No module named 'cultivo'

# ✅ Solución: Usar imports absolutos
from python_forestacion.Entidades.cultivos.cultivo import Cultivo
```

### Error: Singleton no funciona

```python
# ❌ Error común
from python_forestacion.patrones.singleton import singleton
# TypeError: 'module' object is not callable

# ✅ Solución: Importar la función, no el módulo
from python_forestacion.patrones.singleton.singleton import singleton
```

### Error: Circular Import

```python
# ❌ Causa circular import
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

# ✅ Solución: Usar TYPE_CHECKING
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
```

---

## Comandos Útiles

### Desarrollo

```bash
# Encontrar TODOs en código
grep -r "TODO" python_forestacion/ --include="*.py"

# Encontrar magic numbers
grep -r "= [0-9]" python_forestacion/ --include="*.py" | grep -v "constante.py"

# Encontrar lambdas
grep -r "lambda " python_forestacion/ --include="*.py"

# Contar líneas de código
find python_forestacion -name "*.py" -exec wc -l {} + | tail -1

# Verificar PEP 8 (si instalado pylint)
pylint python_forestacion/
```

### Git

```bash
# Ignorar archivos generados
echo "**/integrador.py" >> .gitignore
echo "**/integradorFinal.py" >> .gitignore
echo "**/*.backup_*.py" >> .gitignore
echo "data/" >> .gitignore
echo "data_test/" >> .gitignore

# Commit típico
git add .
git commit -m "feat: agregar tipo de cultivo Tomate"
git push origin main
```

### Limpieza

```bash
# Eliminar __pycache__
find . -type d -name "__pycache__" -exec rm -rf {} +

# Eliminar archivos .pyc
find . -name "*.pyc" -delete

# Eliminar backups
find . -name "*.backup_*.py" -delete

# Eliminar datos de prueba
rm -rf data_test/
```

---

## Recursos Adicionales

### Documentación del Proyecto

- `README.md` - Documentación principal
- `USER_STORIES.md` - Historias de usuario detalladas
- `RUBRICA_EVALUACION.md` - Criterios de evaluación
- `RUBRICA_AUTOMATIZADA.md` - Evaluación automatizada
- `README_BUSCAR_PAQUETE.md` - Herramienta de integración

### Referencias Externas

- [PEP 8](https://pep8.org/) - Style Guide for Python Code
- [Type Hints](https://docs.python.org/3/library/typing.html) - Typing module
- [unittest](https://docs.python.org/3/library/unittest.html) - Testing framework
- [Design Patterns](https://refactoring.guru/design-patterns) - Patrones de diseño

---

## Contacto y Soporte

Para dudas o problemas:
1. Revisar esta guía (CLAUDE.md)
2. Consultar README.md
3. Revisar tests como ejemplos
4. Consultar USER_STORIES.md para casos de uso

---

**Última actualización**: Octubre 2025  
**Versión**: 1.0.0  
**Python requerido**: 3.13+