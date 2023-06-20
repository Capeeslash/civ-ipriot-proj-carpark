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
        float_temp = int(random.gauss(22, 5))
        int_temp = int(float_temp)
        if int_temp < 0:
            int_temp = int_temp * -1
        return int_temp


    def on_detection(self, message):
        """Triggered when a detection occurs"""
        self.client.publish('sensor', message)

    def start_sensing(self):
        """ A blocking event loop that waits for detection events, in this
        case Enter presses"""
        while True:
            print("Press E when 🚗 entered!")
            print("Press X when 🚖 exited!")
            detection = input("E or X> ").upper()
            temperature = self.temperature
            if detection == 'E':
                self.on_detection(f"entered, {temperature} degrees")
                print(f"{temperature}")

            else:
                self.on_detection(f"exited, {temperature} degrees")
                print(f"{temperature}")


if __name__ == '__main__':
    from config_parser import parse_config

    config1 = parse_config("config2.toml")

    sensor1 = Sensor(config1)

    print("Sensor initialized")
    sensor1.start_sensing()


