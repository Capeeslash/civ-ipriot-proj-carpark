""""Demonstrates a simple implementation of an 'event' listener that triggers
a publication via mqtt"""
import random

import mqtt_device


class Sensor(mqtt_device.MqttDevice):

    def __init__(self, config):
        super().__init__(config['config'])



    @property
    def temperature(self):
        """Returns the current temperature"""
        return int(random.gauss(5, 35))

    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('sensor', message)
        print(f"generated temperature: {self.temperature}")

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            print("Press E when 🚗 entered!")
            print("Press X when 🚖 exited!")
            detection = input("E or X> ").upper()
            if detection == 'E':
                self.on_detection(f"entered, {self.temperature}")

            else:
                self.on_detection(f"exited, {self.temperature}")


if __name__ == '__main__':
    from config_parser import parse_config

    config1 = parse_config("config2.toml")

    sensor1 = Sensor(config1)

    print("Sensor initialized")
    sensor1.start_sensing()


