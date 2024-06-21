import paho.mqtt.client as mqtt
import json

broker = "localhost"
port = 1883
topic = "sensor/luz"

def on_connect(client, userdata, flags, rc):
    print("Conectado con código de resultado: " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    device_id = message["device_id"]
    event_time = message["event_time"]
    value = message["value"]
    accuracy = message["accuracy"]

    print(f"Recibiendo información de {device_id} en {event_time}: value={value}, accuracy={accuracy}")

    if value < 50 and accuracy > 0.9:
        print("ENCENDIENDO luces.")
    else:
        print("APAGANDO luces.")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()
