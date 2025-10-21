#!/usr/bin/env python3
"""
Script para corregir automáticamente todos los imports relativos incorrectos
en el proyecto PythonForestal.

Uso:
    python3 fix_imports.py

El script hará backup de los archivos antes de modificarlos.
"""

import os
import re
from pathlib import Path
from datetime import datetime


# Mapeo de imports incorrectos a correctos
REPLACEMENTS = {
    # Entidades - Cultivos
    r'^from cultivo import Cultivo': 'from python_forestacion.Entidades.cultivos.cultivo import Cultivo',
    r'^from arbol import Arbol': 'from python_forestacion.Entidades.cultivos.arbol import Arbol',
    r'^from hortaliza import Hortaliza': 'from python_forestacion.Entidades.cultivos.hortaliza import Hortaliza',
    r'^from tipo_aceituna import TipoAceituna': 'from python_forestacion.Entidades.cultivos.tipo_aceituna import TipoAceituna',
    
    # Entidades - Personal
    r'^from herramienta import Herramienta': 'from python_forestacion.Entidades.personal.herramienta import Herramienta',
    
    # Servicios - Cultivos
    r'^from cultivo_service import CultivoService': 'from python_forestacion.servicios.cultivos.cultivo_service import CultivoService',
    r'^from arbol_service import ArbolService': 'from python_forestacion.servicios.cultivos.arbol_service import ArbolService',
    
    # Excepciones
    r'^from forestacion_exception import ForestacionException': 'from python_forestacion.excepciones.forestacion_exception import ForestacionException',
    r'^from mensajes_exception import': 'from python_forestacion.excepciones.mensajes_exception import',
    
    # Patrones
    r'^from python_forestacion\.patrones\.singleton import singleton$': 'from python_forestacion.patrones.singleton.singleton import singleton',
}


def crear_backup(archivo_path: Path) -> Path:
    """Crea un backup del archivo con timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = archivo_path.with_suffix(f'.backup_{timestamp}{archivo_path.suffix}')
    
    with open(archivo_path, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    return backup_path


def corregir_imports_en_archivo(archivo_path: Path, dry_run=False) -> tuple[bool, int]:
    """
    Corrige los imports en un archivo.
    
    Returns:
        (modificado, num_cambios)
    """
    try:
        with open(archivo_path, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        contenido_original = contenido
        lineas = contenido.split('\n')
        lineas_modificadas = []
        cambios = 0
        
        for linea in lineas:
            linea_modificada = linea
            
            # Aplicar cada reemplazo
            for patron, reemplazo in REPLACEMENTS.items():
                if re.match(patron, linea.strip()):
                    # Preservar indentación
                    indentacion = len(linea) - len(linea.lstrip())
                    linea_modificada = ' ' * indentacion + reemplazo
                    cambios += 1
                    print(f"      - {linea.strip()}")
                    print(f"      + {reemplazo}")
                    break
            
            lineas_modificadas.append(linea_modificada)
        
        contenido_nuevo = '\n'.join(lineas_modificadas)
        
        if contenido_nuevo != contenido_original and not dry_run:
            # Crear backup antes de modificar
            backup_path = crear_backup(archivo_path)
            print(f"    [BACKUP] {backup_path.name}")
            
            # Escribir archivo corregido
            with open(archivo_path, 'w', encoding='utf-8') as f:
                f.write(contenido_nuevo)
        
        return contenido_nuevo != contenido_original, cambios
        
    except Exception as e:
        print(f"    [ERROR] {e}")
        return False, 0


def escanear_directorio(base_path: Path, dry_run=False):
    """Escanea y corrige todos los archivos .py en el directorio."""
    archivos_modificados = 0
    total_cambios = 0
    
    # Buscar todos los archivos .py
    for archivo_path in base_path.rglob('*.py'):
        # Ignorar backups, __pycache__, .venv, etc.
        if any(parte.startswith('.') or parte == '__pycache__' or 'backup' in parte 
               for parte in archivo_path.parts):
            continue
        
        # Ignorar el propio script
        if archivo_path.name == 'fix_imports.py':
            continue
        
        # Mostrar archivo siendo procesado
        ruta_relativa = archivo_path.relative_to(base_path)
        print(f"\n  Procesando: {ruta_relativa}")
        
        modificado, cambios = corregir_imports_en_archivo(archivo_path, dry_run)
        
        if modificado:
            archivos_modificados += 1
            total_cambios += cambios
            if dry_run:
                print(f"    [DRY-RUN] Se harian {cambios} cambio(s)")
            else:
                print(f"    [OK] {cambios} cambio(s) realizado(s)")
        else:
            print(f"    [OK] Sin cambios necesarios")
    
    return archivos_modificados, total_cambios


def main():
    """Función principal."""
    print("=" * 70)
    print("CORRECTOR DE IMPORTS - PythonForestal".center(70))
    print("=" * 70)
    
    # Determinar directorio base
    base_path = Path.cwd()
    print(f"\nDirectorio base: {base_path}")
    
    # Preguntar si hacer dry-run
    respuesta = input("\nDeseas hacer un dry-run (solo ver cambios sin aplicar)? (s/N): ")
    dry_run = respuesta.lower() == 's'
    
    if dry_run:
        print("\n[MODO DRY-RUN] No se modificaran archivos")
    else:
        print("\n[MODO REAL] Se modificaran archivos (se crearan backups)")
        respuesta = input("\nContinuar? (s/N): ")
        if respuesta.lower() != 's':
            print("Operacion cancelada.")
            return
    
    print("\n" + "-" * 70)
    print("ESCANEANDO ARCHIVOS...")
    print("-" * 70)
    
    # Procesar archivos
    archivos_modificados, total_cambios = escanear_directorio(base_path, dry_run)
    
    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN".center(70))
    print("=" * 70)
    print(f"\nArchivos modificados: {archivos_modificados}")
    print(f"Total de cambios: {total_cambios}")
    
    if not dry_run and archivos_modificados > 0:
        print(f"\n[OK] Correcciones aplicadas exitosamente")
        print(f"[INFO] Los backups tienen extension .backup_TIMESTAMP.py")
        print(f"[INFO] Puedes eliminarlos si todo funciona correctamente:")
        print(f"       find . -name '*.backup_*.py' -delete")
    elif dry_run and archivos_modificados > 0:
        print(f"\n[INFO] Ejecuta sin dry-run para aplicar cambios:")
        print(f"       python3 fix_imports.py")
    else:
        print(f"\n[INFO] No se encontraron imports para corregir")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()