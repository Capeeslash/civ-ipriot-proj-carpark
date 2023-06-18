import paho.mqtt.client as mqtt
import json

# Create the settings for our Subscriber
MQTT_HOST = "localhost"   # replace localhost with the computer name that MQTT is running on
MQTT_PORT = 1883  # default MQTT port
MQTT_KEEP_ALIVE = 300  # seconds - this keeps the connection "open"

MQTT_CLIENT_NAME = "geese-on"  # Should (MUST) be unique!
MQTT_TOPIC = "test/geese"  # main topic: test, subtopic: ducks

# Instantiate an MQTT Client
client = mqtt.Client(MQTT_CLIENT_NAME)
# connect to the server/broker
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

# subscribe to the topic
client.subscribe(MQTT_TOPIC)


def on_message_callback(client, userdata, message):
    msg = message
    # decode the message payload into UTF-8 characters
    msg_data = str(msg.payload.decode("UTF-8"))
    data = json.loads(msg_data)

    print()
    print(f"{data['message']}")
    print(f"Topic: {msg.topic} QoS: {msg.qos} Retain: {msg.retain}")


# Listen for messages - call the "callback" when one is received.
client.on_message = on_message_callback

print(f"{MQTT_CLIENT_NAME} is listening on port {MQTT_PORT} for messages with the topic {MQTT_TOPIC}")

client.loop_forever()
