import time
from grove.adc import ADC
from grove.grove_relay import GroveRelay
import json
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse

connection_string = "HostName=nightlight.azure-devices.net;DeviceId=raspberrypi3b+;SharedAccessKey=DinGAe1QF7YGiiUv8UBsliPDKUeA3Fqr7mPglgrZdZE="

adc = ADC()
relay = GroveRelay(5)

device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

print('Connecting')
device_client.connect()
print('Connected')

def handle_method_request(request):
    print('Direct method received -', request.name)
    
    if request.name == "relay_on":
        relay.on()
    elif request.name == "relay_off":
        relay.off()
    
    method_response = MeathodResponse.creat_from_method_request(request, 200)
    device_client.send_method_response(method_respose)

device_client.on_method_request_received = handle_method_request

while True:
    soil_moisture = adc.read(0)
    print("Soild moisture:", soil_moisture)
    
    message = Message(json.dumps({ 'soil_moisture': soil_moisture}))
    device_client.send_message(message)
    
    time.sleep(10)
