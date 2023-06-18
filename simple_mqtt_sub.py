import paho.mqtt.client as mqtt
# from paho.mqtt.client import MQTTMessage

# BROKER, PORT = "localhost", 1883

# def on_message(client, userdata, msg):
#   print(f'Received {msg.payload.decode()}')

# client = paho.Client()
# client.on_message = on_message
# client.connect(BROKER, PORT)
# client.subscribe("lot/sensor")
# client.loop_forever()


MQTT_HOST = "localhost" # name of the device that the MQTT server is running on
MQTT_PORT = 1883 # default port for MQTT
MQTT_KEEP_ALIVE = 300 # number of seconds between each time the sub pings the server

MQTT_CLIENT_NAME = "duck-on"
MQTT_TOPIC = "test/ducks"

client = mqtt.Client(MQTT_CLIENT_NAME)

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

client.subscribe(MQTT_TOPIC)


def on_message_callback(client, userdata, message):
    msg = message
    msg_data = str(msg.payload.decode("UTF-8"))
    print(f"Received: {msg_data}")
    print(f"Topic:    {msg.topic}")
    print(f"QoS:      {msg.qos}")
    print(f"Retain:   {msg.retain}")


client.on_message = on_message_callback

print(f"{MQTT_CLIENT_NAME} is listening on port {MQTT_PORT} for messages with the topic {MQTT_TOPIC}")

client.loop_forever()
