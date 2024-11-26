from grove.adc import ADC

# Initialize the ADC
adc = ADC()

# Read the value from the A0 pin
light_value = adc.read(0)  # 0 indicates A0

print("Light sensor value:", light_value)
