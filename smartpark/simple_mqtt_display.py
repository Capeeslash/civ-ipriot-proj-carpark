#  mport mqtt_device
#  mport time
#  lass Display(mqtt_device.MqttDevice):
#     """Displays the number of cars and the temperature"""
#     def __init__(self, config):
#         super().__init__(config)
#         self.client.on_message = self.on_message
#         self.client.subscribe('display')
#         self.client.loop_forever()

#     def display(self, *args):
#         print('*' * 20)
#         for val in args:
#             print(val)
#             time.sleep(1)

#         print('*' * 20)
#     def on_message(self, client, userdata, msg):
#        data = msg.payload.decode()
#        self.display(*data.split(','))

#  f __name__ == '__main__':
#     config = {'name': 'display',
#      'location': 'L306',
#      'topic-root': "lot",
#      'broker': 'localhost',
#      'port': 1883,
#      'topic-qualifier': 'na'
#      }

#     display = Display(config)

