import paho.mqtt.client as mqtt
from django.http import HttpResponse
import json


PUB_AUTHENTICATE_TOPIC = "SGB/Authenticate"
PUB_WASTE_TOPIC = "SGB/Waste"
SUB_AUTHENTICATE_TOPIC = "SERVER/Authenticate"
SUB_WASTE_TOPIC = "SERVER/waste"

RESPONSE = "No response"

def on_connect(client, userdata, rc):
    # client.subscribe(SUB_AUTHENTICATE_TOPIC,0)
    # client.subscribe(SUB_WASTE_TOPIC,0)
    print("Connected to broker")


def on_message(client, userdata, msg):
	global RESPONSE
	print("Message received from server!")
	RESPONSE = json.loads(msg.payload)
	print(str(msg.payload))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_publish(client, userdata, msg):
	print("Data published")


client = mqtt.Client()

