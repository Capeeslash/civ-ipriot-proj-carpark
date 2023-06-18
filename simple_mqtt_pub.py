import paho.mqtt.client as mqtt

# BROKER, PORT = "localhost", 1883

# client = paho.Client()
# client.connect(BROKER, PORT)
# client.publish("lot/sensor", "Hello from Python")

MQTT_HOST = "localhost" # name of the device that the MQTT server is running on
MQTT_PORT = 1883 # default port for MQTT
MQTT_KEEP_ALIVE = 300 # number of seconds between each time the sub pings the server

MQTT_CLIENT_NAME = "duck-off"
MQTT_TOPIC = "test/ducks"

client = mqtt.Client(MQTT_CLIENT_NAME)

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

client.subscribe(MQTT_TOPIC)

print(f"Sending message to MQTT broker {MQTT_HOST} on port {MQTT_PORT}")
print(f"with the topic {MQTT_TOPIC}...")

message_to_send = "Hello..."

client.publish(MQTT_TOPIC, message_to_send)
