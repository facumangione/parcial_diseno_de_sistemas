"""
Punto de entrada del sistema PythonForestal.
Ejecuta una demostración completa de creación de finca y simulación de riego.
"""

import time
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask


def main():
    print("🌲 Iniciando sistema PythonForestal...\n")

    # Crear servicios principales
    fincas_service = FincasService()
    paquete = Paquete()

    # Crear finca de demostración
    finca = fincas_service.crear_finca(
        id_padron=1001,
        superficie=50.0,
        domicilio="Ruta 8 - Km 35",
        nombre_plantacion="Plantacion Experimental"
    )

    print("✅ Finca creada correctamente:")
    print(f"   ID: {finca.id_padron}")
    print(f"   Superficie: {finca.superficie} m²")
    print(f"   Plantación: {finca.nombre_plantacion}\n")

    # Guardar registro inicial
    paquete.guardar(fincas_service.obtener_registro(), "registro_inicial")
    print("💾 Registro forestal inicial guardado en /data/registro_inicial.dat\n")

    # Configurar sistema de riego
    sensor_temp = TemperaturaReaderTask()
    sensor_hum = HumedadReaderTask()
    controlador = ControlRiegoTask()

    # Registrar observadores
    sensor_temp.agregar_observador(controlador)
    sensor_hum.agregar_observador(controlador)

    print("💧 Sistema de riego listo. Iniciando lecturas...\n")

    # Simular lecturas
    for _ in range(5):
        temp = sensor_temp.leer_temperatura()
        hum = sensor_hum.leer_humedad()
        print(f"Temperatura: {temp}°C | Humedad: {hum}%")
        print(controlador.estado_riego())
        print("-" * 50)
        time.sleep(1.5)

    print("\n✅ Simulación finalizada.")
    paquete.guardar(fincas_service.obtener_registro(), "registro_final")
    print("💾 Registro forestal actualizado guardado en /data/registro_final.dat\n")

    print("🌱 Gracias por utilizar PythonForestal.")


if __name__ == "__main__":
    main()
"import"