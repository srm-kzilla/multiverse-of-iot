import os
import time
import sys
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'JnWmkRvGWxnpUF68TKF4'
light_data = {'status': False, 'time': time.asctime()}
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60) ## Keep Alive time set to 60 (This is the duration for which the socket is open)
client.loop_start()
try:
    while True:
        light_data['status'] = True if input("Press Y to turn on LED (Press any other key to turn it off) : ") == "Y" else False
        light_data['time'] = time.asctime()
        print(str(light_data))
        client.publish('v1/devices/me/telemetry', json.dumps(light_data), 1)
        time.sleep(1)
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()
