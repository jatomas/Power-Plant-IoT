import time
import json
import paho.mqtt.client as mqtt
from grove.grove_moisture_sensor import GroveMoistureSensor
from grove.grove_relay import GroveRelay

moisture_sensor = GroveMoistureSensor(4)
relay = GroveRelay(5)

id = 'jatomasraspi'
client_name = id + 'moisture_sensor_client'
server_command_topic = id + '/commands'
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload['relay_on']:
        relay.on()
    else:
        relay.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

while True:
    soil_moisture = moisture_sensor.moisture
    telemetry = json.dumps({'moisture' : soil_moisture})

    print("Sending telemetry ", telemetry)
    mqtt_client.publish(client_telemetry_topic, telemetry)
    
    time.sleep(10)