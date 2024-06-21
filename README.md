# Taller MQTT IoT - Simulación de Sensor de Luz

## Descripción

Este proyecto simula una solución IoT utilizando el protocolo MQTT. Incluye un sensor de luz que publica datos y un controlador de luces que suscribe a estos datos para decidir si encender o apagar las luces de una habitación.

## Requisitos

- **Mosquitto**: Broker MQTT para la comunicación.
- **Paho-MQTT**: Biblioteca Python para la implementación de clientes MQTT.
- **Python 3**: Necesario para ejecutar los scripts de Python.

## Instalación de Dependencias

Para instalar las dependencias necesarias, se sigue los siguientes pasos:

1. **Instalar Mosquitto:**
   - Líneas de código para instalar Mosquitto:
     ```bash
     sudo apt update
     sudo apt install mosquitto mosquitto-clients -y
     ```

2. **Instalar Paho-MQTT:**
   - Instalar la biblioteca Paho-MQTT para Python utilizando pip:
     ```bash
     pip install paho-mqtt
     ```

## Configuración y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto:

1. **Configuración del Broker Mosquitto:**
   - Asegúrate de que Mosquitto esté instalado y ejecutándose correctamente. Para ello, ejecuta el script `start_mosquitto.sh`:
     ```bash
     ./start_mosquitto.sh
     ```

2. **Ejecutar el Sensor de Luz (Publicador):**
   - Abre una terminal y navega hasta el directorio donde tienes los archivos del proyecto.
   - Ejecuta el script `publish_sensor.sh` para simular la emisión de datos del sensor de luz:
     ```bash
     ./publish_sensor.sh
     ```

3. **Ejecutar el Controlador de Luces (Suscriptor):**
   - Abre otra terminal en el mismo directorio del proyecto.
   - Ejecuta el script `encendedor.py` para controlar el encendido y apagado de las luces:
     ```bash
     python3 encendedor.py
     ```
     
## Autor

Luis Armijos
