import time
from random import randrange, uniform
import json
from datetime import datetime

import paho.mqtt.client as mqtt

MQTT_HOST = "localhost"
MQTT_PORT = 1883 # default port for MQTT
MQTT_KEEP_ALIVE = 300 # number of seconds between each time the sub pings the server

MQTT_CLIENT_NAME = "duck-off"
MQTT_TOPIC = "test/ducks"

client = mqtt.Client(MQTT_CLIENT_NAME)

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)


print(f"Sending message to MQTT broker {MQTT_HOST} on port {MQTT_PORT}")
print(f"with the topic {MQTT_TOPIC}...")

message_to_send = "Hello..."

while True:
    time.sleep(5)
    temperature = uniform(20, 25)
    now = datetime.now().strftime("%Y-%m-%dT%H:%SZ+0800")
    message_data = {
        "client": MQTT_CLIENT_NAME,
        "temp": temperature,
        "datetime": now
    }
    message_to_send = json.dumps(message_data)
    print(f"Temperature is {temperature}")
    client.publish(MQTT_TOPIC, message_to_send)

