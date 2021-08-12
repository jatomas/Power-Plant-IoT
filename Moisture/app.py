import time
from grove.grove_moisture_sensor import GroveMoistureSensor

moisture_sensor = GroveMoistureSensor(4)

while True:
    soil_moisture = moisture_sensor.moisture
    print("Soil moisture:", soil_moisture)

    time.sleep(2)