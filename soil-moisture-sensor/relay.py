from grove.grove_relay import GroveRelay
import time
relay = GroveRelay(5)

relay.on()
print("Relay on")
time.sleep(10)
relay.off()
print("Relay off")
time.sleep(10)
relay.on()
print("Relay on")
time.sleep(10)
relay.off()
print("Relay off")
