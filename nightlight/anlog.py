import time
from grovepi import *

# Set the analog port
analog_port = 0

while True:
    try:
        # Read the value from A0
        sensor_value = analogRead(analog_port)
        print("Analog Value from A0: ", sensor_value)
        time.sleep(1)
    except IOError:
        print("Error reading from sensor")
