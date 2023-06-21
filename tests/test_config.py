import unittest
import tomli  # you can use toml, json,yaml, or ryo for your config file
from smartpark.config_parser import parse_config


class TestConfigParsing(unittest.TestCase):
    def test_parse_config_has_correct_location_and_spaces(self):
        config_string = '''
        [parking_lot]
        location = "Moondalup City Square Parking"
        total_spaces = 192
        broker_host = "localhost"
        broker_port = 1883
        '''

        config = parse_config('testconfig.toml')
        self.assertEqual(config['location'], "Moondalup City Square Parking")
        self.assertEqual(config['total_spaces'], 192)