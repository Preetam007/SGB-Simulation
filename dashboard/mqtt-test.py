import paho.mqtt.client as mqtt
from django.http import HttpResponse
import json
import time

PUB_AUTHENTICATE_TOPIC = "SGB/Authenticate"
PUB_WASTE_TOPIC = "SGB/Waste"
SUB_AUTHENTICATE_TOPIC = "SERVER/Authenticate"
SUB_WASTE_TOPIC = "SERVER/Waste"

RESPONSE = "No response"
start_time = 0
time_elapsed = 0

def on_connect(client, userdata, rc):
    # client.subscribe(SUB_AUTHENTICATE_TOPIC,0)
    # client.subscribe(SUB_WASTE_TOPIC,0)
    print("Connected to broker")


def on_message(client, userdata, msg):
	global RESPONSE
	global start_time
	global time_elapsed
	print("Duration to receive message: ",time.time())
	time_elapsed = time.time() - start_time
	print("MQTT Execution time: ",time_elapsed * 1000) # convert into milliseconds
	print("Message received from server!")
	RESPONSE = json.loads(msg.payload)
	print(str(msg.payload))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_publish(client, userdata, msg):
	global start_time
	start_time = time.time()
	print("Start time: ",start_time)
	print("Data published")


client = mqtt.Client()

