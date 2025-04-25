from time import sleep
from grove.adc import ADC
from grove.grove_relay import GroveRelay
import json
import paho.mqtt.client as mqtt

adc = ADC()
relay = GroveRelay(5)

id = "7a159771-dbf3-4736-8de2-962737f88250"

client_telementry_topic = id +'/telemetry'
server_command_topic = id +'/command'
client_name = id + 'soilmoisturesensor_client'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect("test.mosquitto.org")

def handle_message(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    
    if payload['relay_on']:
        relay.on()
    else:
        relay.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_message

while True:
    soil_moisture = adc.read(0)
    print("Soil moisture:", soil_moisture)
    mqtt_client.publish(client_telementry_topic, json.dumps({"soil_moisture": soil_moisture}))
    sleep(10)
