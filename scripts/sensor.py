import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime

def publish_sensor():
    broker = "localhost"
    port = 1883
    topic = "sensor/luz"

    client = mqtt.Client()
    client.connect(broker, port)

    while True:
        data = {
            "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
            "event_time": "2025-06-12T14:07:46.580465",
            "value": 60,
            "accuracy": 0.98
        }

        client.publish(topic, json.dumps(data))
        print(f"Publicando: {data}")
        time.sleep(5)

if __name__ == "__main__":
    publish_sensor()
