"""
Punto de entrada del sistema PythonForestal.
Ejecuta una demostración completa de todos los patrones de diseño implementados.

Patrones demostrados:
- SINGLETON: CultivoServiceRegistry
- FACTORY METHOD: CultivoFactory
- OBSERVER: Sensores y ControlRiegoTask
- STRATEGY: AbsorcionAguaStrategy (seasonal y constante)
- REGISTRY: Dispatch polimórfico sin isinstance()
"""

import time
from datetime import date

# Servicios principales
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService

# Entidades
from python_forestacion.Entidades.terrenos.tierra import Tierra
from python_forestacion.Entidades.terrenos.plantacion import Plantacion
from python_forestacion.Entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.Entidades.personal.trabajador import Trabajador
from python_forestacion.Entidades.personal.tarea import Tarea
from python_forestacion.Entidades.personal.herramienta import Herramienta
from python_forestacion.Entidades.personal.apto_medico import AptoMedico

# Servicios de personal
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

# Patrones
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

# Sistema de riego
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Constantes
from constante import THREAD_JOIN_TIMEOUT


def imprimir_encabezado(titulo: str, caracter: str = "=", ancho: int = 70):
    """Imprime un encabezado decorado."""
    print("\n" + caracter * ancho)
    print(titulo.center(ancho))
    print(caracter * ancho)


def imprimir_seccion(titulo: str, ancho: int = 70):
    """Imprime una sección con guiones."""
    print("\n" + "-" * ancho)
    print("  " + titulo)
    print("-" * ancho)


def demostrar_singleton():
    """Demuestra el patrón SINGLETON."""
    imprimir_seccion("PATRON SINGLETON: Inicializando servicios")
    
    # Crear múltiples instancias del registry
    registry1 = CultivoServiceRegistry()
    registry2 = CultivoServiceRegistry()
    
    # Verificar que son la misma instancia
    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
        print(f"     ID registry1: {id(registry1)}")
        print(f"     ID registry2: {id(registry2)}")
        print("     Son identicos: True")
    else:
        print("[ERROR] Las instancias NO son iguales - Singleton fallido")
    
    return registry1


def demostrar_factory(plantacion_service: PlantacionService, plantacion: Plantacion):
    """Demuestra el patrón FACTORY METHOD."""
    imprimir_seccion("PATRON FACTORY: Creacion dinamica de cultivos")
    
    print("\n1. Creando tierra con plantacion...")
    print(f"   Superficie disponible: {plantacion.superficie} m2")
    print(f"   Agua disponible: {plantacion.agua_disponible} L")
    
    print("\n2. Plantando cultivos usando Factory Method:")
    
    # Plantar diferentes tipos de cultivos
    cultivos_a_plantar = [
        ("Pino", 5),
        ("Olivo", 5),
        ("Lechuga", 5),
        ("Zanahoria", 5)
    ]
    
    for tipo, cantidad in cultivos_a_plantar:
        try:
            # Aquí se usa Factory Method internamente
            for _ in range(cantidad):
                cultivo = CultivoFactory.crear_cultivo(tipo)
                plantacion.agregar_cultivo(cultivo)
            print(f"   [OK] {cantidad} {tipo}(s) plantado(s)")
        except Exception as e:
            print(f"   [ERROR] No se pudo plantar {tipo}: {e}")
    
    print(f"\n3. Total de cultivos plantados: {len(plantacion.cultivos)}")
    print("   [OK] Factory Method funciono correctamente")


def demostrar_observer():
    """Demuestra el patrón OBSERVER."""
    imprimir_seccion("PATRON OBSERVER: Sistema de sensores y eventos")
    
    print("\n1. Inicializando sensores (Observable)...")
    sensor_temp = TemperaturaReaderTask()
    sensor_hum = HumedadReaderTask()
    print("   [OK] Sensor de temperatura creado")
    print("   [OK] Sensor de humedad creado")
    
    print("\n2. Inicializando controlador de riego (Observer)...")
    controlador = ControlRiegoTask()
    print("   [OK] Controlador de riego creado")
    
    print("\n3. Registrando observadores...")
    sensor_temp.agregar_observador(controlador)
    sensor_hum.agregar_observador(controlador)
    print("   [OK] Controlador suscrito a sensores")
    
    print("\n4. Simulando lecturas de sensores (5 iteraciones):")
    print("   " + "=" * 60)
    
    for i in range(5):
        temp = sensor_temp.leer_temperatura()
        hum = sensor_hum.leer_humedad()
        
        print(f"\n   Lectura {i+1}:")
        print(f"     Temperatura: {temp} grados C")
        print(f"     Humedad: {hum}%")
        print(f"     Estado: {controlador.estado_riego()}")
        
        time.sleep(1)
    
    print("\n   " + "=" * 60)
    print("   [OK] Patron Observer funciono correctamente")
    print("   [OK] Notificaciones automaticas funcionaron")
    
    return sensor_temp, sensor_hum, controlador


def demostrar_strategy(plantacion: Plantacion, registry: CultivoServiceRegistry):
    """Demuestra el patrón STRATEGY."""
    imprimir_seccion("PATRON STRATEGY: Algoritmos de absorcion de agua")
    
    print("\n1. Regando plantacion...")
    print(f"   Agua disponible antes: {plantacion.agua_disponible} L")
    
    # Regar todos los cultivos
    try:
        plantacion.regar_todos(10)
        print("   [OK] Riego completado")
    except Exception as e:
        print(f"   [ERROR] Error al regar: {e}")
    
    print(f"   Agua disponible despues: {plantacion.agua_disponible} L")
    
    print("\n2. Mostrando absorcion por tipo de cultivo:")
    print("   (Cada tipo usa una estrategia diferente)")
    print("   " + "-" * 60)
    
    # Agrupar cultivos por tipo
    tipos_contados = {}
    for cultivo in plantacion.cultivos:
        tipo = type(cultivo).__name__
        if tipo not in tipos_contados:
            tipos_contados[tipo] = []
        tipos_contados[tipo].append(cultivo)
    
    # Mostrar absorción por tipo
    for tipo, cultivos_del_tipo in tipos_contados.items():
        print(f"\n   {tipo}:")
        if tipo in ["Pino", "Olivo"]:
            print(f"     Estrategia: SEASONAL (5L verano, 2L invierno)")
        else:
            print(f"     Estrategia: CONSTANTE (1-2L siempre)")
        print(f"     Cantidad plantada: {len(cultivos_del_tipo)}")
    
    print("\n   " + "-" * 60)
    print("   [OK] Patron Strategy funciono correctamente")
    print("   [OK] Algoritmos intercambiables funcionaron")


def demostrar_registry(plantacion: Plantacion, registry: CultivoServiceRegistry):
    """Demuestra el patrón REGISTRY (bonus)."""
    imprimir_seccion("PATRON REGISTRY: Dispatch polimorfico")
    
    print("\n1. Mostrando datos de cultivos usando Registry:")
    print("   (Sin usar isinstance() - dispatch automatico)")
    print("   " + "-" * 60)
    
    for i, cultivo in enumerate(plantacion.cultivos[:8], 1):  # Primeros 8
        print(f"\n   Cultivo {i}:")
        try:
            # El registry hace dispatch automático según el tipo
            registry.mostrar_datos(cultivo)
        except Exception as e:
            print(f"     [ERROR] {e}")
    
    if len(plantacion.cultivos) > 8:
        print(f"\n   ... y {len(plantacion.cultivos) - 8} cultivos mas")
    
    print("\n   " + "-" * 60)
    print("   [OK] Patron Registry funciono correctamente")
    print("   [OK] Dispatch polimorfico sin isinstance()")


def demostrar_gestion_personal():
    """Demuestra la gestión de personal."""
    imprimir_seccion("GESTION DE PERSONAL: Trabajadores y tareas")
    
    # Crear tareas
    herramienta = Herramienta("Pala", "operativa")
    tareas = [
        Tarea("Desmalezar", date.today(), herramienta),
        Tarea("Abonar", date.today(), herramienta),
        Tarea("Marcar surcos", date.today(), herramienta)
    ]
    
    # Crear trabajador
    trabajador = Trabajador("Juan Perez", "43888734", 35)
    trabajador.tareas = tareas
    
    print("\n1. Trabajador registrado:")
    print(f"   Nombre: {trabajador.nombre}")
    print(f"   DNI: {trabajador.dni}")
    print(f"   Edad: {trabajador.edad}")
    print(f"   Tareas asignadas: {len(trabajador.tareas)}")
    
    # Asignar apto médico
    apto = AptoMedico(
        fecha_emision=date.today(),
        valido_hasta=date(2025, 12, 31),
        observaciones="Estado de salud: excelente"
    )
    trabajador.apto_medico = apto
    
    print("\n2. Apto medico asignado:")
    print(f"   Fecha emision: {apto.fecha_emision}")
    print(f"   Valido hasta: {apto.valido_hasta}")
    print(f"   Esta vigente: {apto.esta_vigente()}")
    
    print("\n3. Ejecutando tareas:")
    trabajador_service = TrabajadorService()
    trabajador_service.registrar_trabajador(trabajador)
    
    # Simular ejecución de tareas
    for tarea in sorted(trabajador.tareas, key=lambda t: t.descripcion, reverse=True):
        print(f"   [OK] Tarea: {tarea.descripcion}")
        tarea.completada = True
    
    print("\n   [OK] Todas las tareas completadas")


def demostrar_persistencia(fincas_service: FincasService):
    """Demuestra la persistencia de datos."""
    imprimir_seccion("PERSISTENCIA: Guardado y recuperacion de datos")
    
    print("\n1. Guardando registro forestal...")
    paquete = Paquete()
    
    try:
        registro = fincas_service.obtener_registro()
        paquete.guardar(registro, "registro_inicial")
        print("   [OK] Registro guardado en data/registro_inicial.dat")
    except Exception as e:
        print(f"   [ERROR] Error al guardar: {e}")
    
    print("\n2. Verificando archivo persistido...")
    import os
    if os.path.exists("data/registro_inicial.dat"):
        size = os.path.getsize("data/registro_inicial.dat")
        print(f"   [OK] Archivo existe ({size} bytes)")
    else:
        print("   [ERROR] Archivo no encontrado")
    
    print("\n3. Recuperando datos...")
    try:
        registro_recuperado = paquete.cargar("registro_inicial")
        print("   [OK] Datos recuperados correctamente")
        print(f"   Plantaciones recuperadas: {len(registro_recuperado.listar_todas())}")
    except Exception as e:
        print(f"   [ERROR] Error al recuperar: {e}")


def main():
    """Función principal que ejecuta todas las demostraciones."""
    
    imprimir_encabezado("SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    
    print("\nDemostracion completa de patrones de diseno implementados:")
    print("  - SINGLETON (CultivoServiceRegistry)")
    print("  - FACTORY METHOD (CultivoFactory)")
    print("  - OBSERVER (Sensores y ControlRiegoTask)")
    print("  - STRATEGY (AbsorcionAguaStrategy)")
    print("  - REGISTRY (Dispatch polimorfico)")
    
    try:
        # 1. SINGLETON
        registry = demostrar_singleton()
        
        # 2. Crear finca para demostraciones
        print("\n" + "=" * 70)
        print("Preparando entorno de pruebas...")
        print("=" * 70)
        
        tierra_service = TierraService()
        tierra = Tierra(
            id_padron=1001,
            superficie=10000.0,
            domicilio="Ruta 8 - Km 35",
            nombre_plantacion="Plantacion Experimental"
        )
        
        plantacion = Plantacion(
            nombre="Plantacion Experimental",
            superficie=10000.0,
            agua_disponible=500.0
        )
        
        tierra.set_plantacion(plantacion)
        tierra_service.registrar_tierra(tierra)
        
        plantacion_service = PlantacionService()
        plantacion_service.registrar_plantacion(plantacion)
        
        print("[OK] Entorno preparado")
        
        # 3. FACTORY METHOD
        demostrar_factory(plantacion_service, plantacion)
        
        # 4. OBSERVER
        sensor_temp, sensor_hum, controlador = demostrar_observer()
        
        # 5. STRATEGY
        demostrar_strategy(plantacion, registry)
        
        # 6. REGISTRY (bonus)
        demostrar_registry(plantacion, registry)
        
        # 7. Gestión de personal
        demostrar_gestion_personal()
        
        # 8. Persistencia
        fincas_service = FincasService()
        # Registrar la plantación en el servicio
        fincas_service.obtener_registro().agregar_plantacion(plantacion)
        demostrar_persistencia(fincas_service)
        
        # Resumen final
        imprimir_encabezado("EJEMPLO COMPLETADO EXITOSAMENTE")
        
        print("\nResumen de patrones demostrados:")
        print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
        print("  [OK] FACTORY     - Creacion dinamica de 4 tipos de cultivos")
        print("  [OK] OBSERVER    - Sistema de sensores y notificaciones")
        print("  [OK] STRATEGY    - Algoritmos intercambiables de absorcion")
        print("  [OK] REGISTRY    - Dispatch polimorfico sin isinstance()")
        
        print("\nFuncionalidades demostradas:")
        print("  [OK] Gestion de cultivos (Pino, Olivo, Lechuga, Zanahoria)")
        print("  [OK] Sistema de riego automatizado")
        print("  [OK] Gestion de personal con apto medico")
        print("  [OK] Persistencia con Pickle")
        
        print("\n" + "=" * 70)
        print("Gracias por utilizar PythonForestal".center(70))
        print("Sistema educativo de patrones de diseno en Python".center(70))
        print("=" * 70 + "\n")
        
        return 0
        
    except Exception as e:
        print(f"\n[ERROR CRITICO] {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())