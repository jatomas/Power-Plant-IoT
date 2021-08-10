import json
import paho.mqtt.client as mqtt
import time
from seeed_dht import DHT

sensor = DHT("11", 16)

id = 'jatomasraspi'
client_name = id + 'temperature_sensor_client'
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

print("MQTT connected!")

while True:
    _, temp = sensor.read()
    print(f'Temperature {temp}°C')

    telemetry = json.dumps({'temperature' : temp})

    print("Sending telemetry ", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(3600)