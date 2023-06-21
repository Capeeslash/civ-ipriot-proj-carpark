import unittest
from unittest.mock import patch
from test_simple_mqtt_carpark import CarPark


class TestCarPark(unittest.TestCase):
    def setUp(self):
        # Mock the MQTT client and disable the loop
        self.patcher = patch('paho.mqtt.client.Client')
        self.mock_client_class = self.patcher.start()
        self.mock_client = self.mock_client_class.return_value
        self.mock_client.loop_start.return_value = None
        self.mock_client.loop_stop.return_value = None

        # Create a CarPark instance
        config = {
            'carpark_location': 'Test Location',
            'total_spaces': 192,
            'total_cars': 0,
            'name': 'parking-lot',
            'location': '',
            'topic-root': '',
            'topic-qualifier': '',
            'broker': '',
            'port': ''
        }
        self.car_park = CarPark(config)

    def tearDown(self):
        # Stop the MQTT client patcher
        self.patcher.stop()

    def test_no_negative_cars(self):
        self.car_park.total_cars = 2

        self.car_park.on_car_exit()
        self.car_park.on_car_exit()
        self.car_park.on_car_exit()

        self.assertEqual(self.car_park.total_cars, 0)
