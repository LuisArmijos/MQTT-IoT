#!/bin/bash

# Iniciar el servicio Mosquitto
echo "Iniciando el broker Mosquitto..."
sudo systemctl start mosquitto
sudo systemctl enable mosquitto

echo "Broker Mosquitto iniciado y habilitado para iniciar automáticamente al arrancar el sistema."
