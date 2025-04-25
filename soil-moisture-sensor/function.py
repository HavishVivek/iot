import time
import json
from azure.iot.device import IoTHubDeviceClient, Message

# Replace with your actual device connection string
connection_string = "HostName=nightlight.azure-devices.net;DeviceId=raspberrypi3b;SharedAccessKey=Yv5bZ7385vs1WxeSZksWSri77EEdQLrhbLZZd/17egs="

# Connect to IoT Hub
device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)
device_client.connect()

print("Connected to Azure IoT Hub")

while True:
    # Create a simple message
    data = { "status": "working" }
    message = Message(json.dumps(data))

    print("Sending message:", data)
    device_client.send_message(message)

    time.sleep(10)
