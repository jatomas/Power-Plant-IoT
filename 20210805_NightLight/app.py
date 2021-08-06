import json
import paho.mqtt.client as mqtt
import time
#from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_led import GroveLed

#light_sensor = GroveLightSensor(4)
led = GroveLed(5)

id = 'jatomasraspi'
client_name = id + 'nightlight_client'
server_command_topic = id + '/commands'
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

print("MQTT connected!")

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload['led_on']:
        led.on()
    else:
        led.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

i = 0

while True:
 #   light = light_sensor.light
 #   print('Light level:', light)
    telemetry = json.dumps({'light' : 100+i})

    print("Sending telemetry ", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    i += 1    
    
    time.sleep(1)