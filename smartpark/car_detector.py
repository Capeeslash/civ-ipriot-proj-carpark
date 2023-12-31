#  import random
#  import threading
#  import time
#  import tkinter as tk
#  from typing import Iterable
#  from car_park_display import WindowedDisplay
#  class CarDetector:
#      """Provides a couple of simple buttons that can be used to represent
#      a sensor detecting a car. This is a skeleton only."""
#
#      def __init__(self):
#          self.root = tk.Tk()
#          self.root.title("Car Detector ULTRA")
#
#          self.btn_incoming_car = tk.Button(
#              self.root, text='🚘 Incoming Car', font=('Arial', 50), cursor='right_side', command=self.incoming_car)
#          self.btn_incoming_car.pack(padx=10, pady=5)
#          self.btn_outgoing_car = tk.Button(
#              self.root, text='Outgoing Car 🚘',  font=('Arial', 50), cursor='bottom_left_corner',
#              command=self.outgoing_car)
#          self.btn_outgoing_car.pack(padx=10, pady=5)
#
#          self.root.mainloop()
#
#      def incoming_car(self):
#          implement this method to publish the detection via MQTT
#          print("Car goes in")
#
#      def outgoing_car(self):
#          implement this method to publish the detection via MQTT
#          print("Car goes out")
#
#
#  if __name__ == '__main__':
#      CarDetector()
