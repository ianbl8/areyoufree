#!/usr/bin/python3

# client_sub.py
# Ian Blake
#
# to check MQTT messages are reaching broker

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys

# define event callbacks
def on_connect(client, userdata, flags, rc):
    print("MQTT connection result: " + str(rc))

def on_message(client, obj, msg):
    print("Topic: " + msg.topic + "; Payload:" + str(msg.payload))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed, QOS granted: " + str(granted_qos))

mqttc = mqtt.Client(transport = "websockets")

# assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.on_subscribe = on_subscribe

url = urlparse("ws://broker.hivemq.com:8000/mqtt/ianbl8/home")
base_topic = url.path[1:]
print(base_topic)
if (url.username):
    mqttc.username_pw_set(url.username, url.password)

mqttc.connect(url.hostname, url.port)

# start subscribe
mqttc.subscribe(base_topic + "/#")
mqttc.loop_forever()

# exit on error
rc = 0
while rc == 0:
    rc = mqttc.loop()

