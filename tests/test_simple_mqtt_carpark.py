from datetime import datetime
import random
import mqtt_device
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['total_spaces']
        self.total_cars = config['total_cars']
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.client.loop_forever()

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return max(available, 0)


    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(
            (
                f"TIME: {readable_time}, "
                + f"SPACES: {self.available_spaces}, "

            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"SPACES: {self.available_spaces}, "

        )
        self.client.publish('display', message)

    def on_car_entry(self):
        if self.available_spaces <= 0:
            self.total_cars +=0
        else:
            self.total_cars += 1
            self._publish_event()

    def on_car_exit(self):
        if self.total_cars <= 0:
            self.total_cars
        else:
            self.total_cars -= 1
            self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        print("received message:", msg.topic, msg.payload.decode())
        payload = msg.payload.decode()
        temperature_start_index = payload.index(', ') + len(', ')
        temperature_end_index = payload.index(' degrees')
        self.temperature = int(payload[temperature_start_index:temperature_end_index])
        if 'exited' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()


if __name__ == '__main__':
    from config_parser import parse_config
    config = parse_config("config.toml")
    car_park = CarPark(config)
    print("Carpark initialized")

