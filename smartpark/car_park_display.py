import random
import threading
import time
import tkinter as tk
from typing import Iterable
import mqtt_device


class WindowedDisplay:

    DISPLAY_INIT = '– – –'
    SEP = ':'  # field name separator

    def __init__(self, title: str, display_fields: Iterable[str]):
        self.window = tk.Tk()
        self.window.title(f'{title}: Parking')
        self.window.geometry('800x400')
        self.window.resizable(False, False)
        self.display_fields = display_fields

        self.gui_elements = {}
        for i, field in enumerate(self.display_fields):
            # create the elements
            self.gui_elements[f'lbl_field_{i}'] = tk.Label(
                self.window, text=field + self.SEP, font=('Arial', 50))
            self.gui_elements[f'lbl_value_{i}'] = tk.Label(
                self.window, text=self.DISPLAY_INIT, font=('Arial', 50))

            # position the elements
            self.gui_elements[f'lbl_field_{i}'].grid(
                row=i, column=0, sticky=tk.E, padx=5, pady=5)
            self.gui_elements[f'lbl_value_{i}'].grid(
                row=i, column=2, sticky=tk.W, padx=10)

    def show(self):
        """Display the GUI. Blocking call."""
        self.window.mainloop()

    def update(self, updated_values: dict):
        """Update the values displayed in the GUI. Expects a dictionary
        with keys matching the field names passed to the constructor."""
        for field in self.gui_elements:
            if field.startswith('lbl_field'):
                field_value = field.replace('field', 'value')
                self.gui_elements[field_value].configure(
                    text=updated_values[self.gui_elements[field].cget('text').rstrip(self.SEP)])
        self.window.update()


class Display(mqtt_device.MqttDevice):
    """Provides a simple display of the car park status. This is a skeleton only.
    The class is designed to be customizable without requiring and understanding of tkinter or threading."""
    # determines what fields appear in the UI
    fields = ['Available bays', 'Temperature', 'At']

    def __init__(self, config):
        super().__init__(config['config'])
        self.window = WindowedDisplay(
            'Moondalup', Display.fields)
        updater = threading.Thread(target=self.check_updates)
        updater.daemon = True
        updater.start()
        self.window.show()

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val)
            time.sleep(1)

        print('*' * 20)

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        self.display(*payload.split(','))
        # TODO: Parse the message and extract free spaces,
        #  temperature, time

    def check_updates(self):
        self.client.on_message = self.on_message
        self.client.subscribe('display')
        self.client.loop_forever()

        while True:
            # NOTE: Dictionary keys *must* be the same as the class fields
            field_values = dict(zip(Display.fields, [
                # TODO: change this so that it shows actual spaces and temp values
                f'{random.randint(0, 150):03d}',
                f'{random.randint(0, 45):02d}℃',
                time.strftime("%H:%M:%S")]))
            # Pretending to wait on updates from MQTT
            time.sleep(random.randint(1, 10))
            # When you get an update, refresh the display.
            self.window.update(field_values)


if __name__ == '__main__':
    from config_parser import parse_config

    config3 = parse_config("config3.toml")
    display = Display(config3)
    print("Carpark Display initialized")
