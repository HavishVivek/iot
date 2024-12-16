import time
from seeed_dht import DHT
import paho.mqtt.client as mqtt
import json
from os import path
import csv
from datetime import datetime

# Sensor setup
sensor = DHT("11", 5)

# MQTT and file setup
id = '7a159771-dbf3-4736-8de2-962737f88250'
client_telemetry_topic = id + '/telemetry'
client_name = id + 'temperature_sensor_server'

mqtt_client = mqtt.Client(client_name)

# CSV file setup
temperature_file_name = 'temperature.csv'
fieldnames = ['date', 'temperature']

if not path.exists(temperature_file_name):
    with open(temperature_file_name, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

# Callback function to handle incoming messages
def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    
    # Save to CSV
    with open(temperature_file_name, mode='a') as temperature_file:
        temperature_writer = csv.DictWriter(temperature_file, fieldnames=fieldnames)
        temperature_writer.writerow({
            'date': datetime.now().astimezone().replace(microsecond=0).isoformat(),
            'temperature': payload['temperature']
        })

# Set up the MQTT client
mqtt_client.on_message = handle_telemetry  # Link callback
mqtt_client.connect('test.mosquitto.org')
mqtt_client.subscribe(client_telemetry_topic)  # Subscribe to topic
mqtt_client.loop_start()

print("Server is ready and waiting for telemetry data!")

# Keep the server running
while True:
    time.sleep(1)