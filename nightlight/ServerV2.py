import time
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_led import GroveLed
import json
import paho.mqtt.client as mqtt
from paho.mqtt.client import Client, MQTTMessage

light_sensor = GroveLightSensor(0)  # Port A0
led = GroveLed(5)  # Port D5

id = '7a159771-dbf3-4736-8de2-962737f88250'

client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'
client_name = id + '_nightlight_client'

mqtt_client = mqtt.Client(client_name)

try:
    mqtt_client.connect('test.mosquitto.org')
except Exception as e:
    print("MQTT connection error:", e)
    exit(1)

mqtt_client.loop_start()

def handle_command(client: Client, userdata, message: MQTTMessage):
    try:
        payload = json.loads(message.payload.decode())
        print(f"Message received: {payload}")

        if 'led_on' in payload:
            if payload['led_on']:
                led.on()
            else:
                led.off()
    except Exception as e:
        print("Error processing message:", e)

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

try:
    while True:
        light = light_sensor.light
        print(f"Message received: {{'light': {light}}}")

        # Determine if the LED should be on or off
        led_on = light < 300  # Example threshold
        print(f"Sending message: {{'led_on': {led_on}}}")

        # Publish the LED state
        mqtt_client.publish(server_command_topic, json.dumps({'led_on': led_on}))

        time.sleep(5)
except KeyboardInterrupt:
    print("Exiting...")
    mqtt_client.loop_stop()
    mqtt_client.disconnect()