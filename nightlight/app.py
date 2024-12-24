from time import sleep
from grove.grove_light_sensor_v1_2 import GroveLightSensor # type: ignore
from grove.grove_led import GroveLed # type: ignore


light_sensor = GroveLightSensor(0)
led = GroveLed(5)

while True:
    light = light_sensor.light
    print('Light level:', light)

    if light > 300:
        led.on()
    else:
        led.off()
    
    sleep(1)
