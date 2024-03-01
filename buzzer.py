import pigpio
from time import sleep

class Buzzer:
    def __init__(self) -> None:
        print("Initialize Buzzer")
        self.pi = pigpio.pi()
        self.buzzer_pin = 24
        self.pi.write(self.buzzer_pin, 0)

    def turn_on_buzzer(self):
        # Turn on the buzzer
        self.pi.write(self.buzzer_pin, 1)
        print("Buzzer is ON")
        
        # Wait for the specified duration
        sleep(3)
        
        # Turn off the buzzer
        self.pi.write(self.buzzer_pin, 0)
        print("Buzzer is OFF")

    def stop(self):
        print("Stop Buzzer")
        self.pi.write(self.buzzer_pin, 0)
        self.pi.stop()

