from datetime import datetime
import random
import mqtt_device
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config['config'])
        self.total_spaces = config['config']['total-spaces']
        self.total_cars = config['config']['total-cars']
        self._temperature = None
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.client.loop_forever()

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return max(available, 0)

    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        temperature = int(random.gauss(5, 35))
        print(
            (
                f"TIME: {readable_time}, "
                + f"SPACES: {self.available_spaces}, "
                + f"TEMPC: {temperature}"
            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"SPACES: {self.available_spaces}, "
            + f"TEMPC: {temperature}"
        )
        self.client.publish('display', message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()

    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    def on_message(self, client, userdata, msg: MQTTMessage):
        print("received message:", msg.topic, msg.payload.decode())
        payload = msg.payload.decode()
        if 'exited' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()


if __name__ == '__main__':
    from config_parser import parse_config
    config = parse_config("config.toml")
    car_park = CarPark(config)
    print("Carpark initialized")

