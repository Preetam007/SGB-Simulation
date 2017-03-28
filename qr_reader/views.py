from django.shortcuts import render
from django.http import HttpResponse
from . import mqtt as mqtt_module
import time

MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60




def index(request):
	return HttpResponse("<h2>QR_Reader module is loaded here</h2>")

def read(request):
	# this loads the view inside templates folder inside this app
	# but django treats all the templates folder of different apps as one single /templates folder
	# so it will be wise to namespace them according to the app to remove any possibility of conflict 
	return render(request,"qr_reader/waste_bin.html")

def mqtt_ajax(request):
	decoded_qr =  request.POST.get("code","error getting code")

	client = mqtt_module.client
	client.on_connect = mqtt_module.on_connect
	client.on_subscribe = mqtt_module.on_subscribe
	client.on_message = mqtt_module.on_message
	client.on_publish = mqtt_module.on_publish
	
	# establish mqtt connection subscribe to message topic from server
	client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
	client.loop_start()
	# publish qr_code to server
	client.subscribe(mqtt_module.SUB_AUTHENTICATE_TOPIC,0)
	client.subscribe(mqtt_module.SUB_WASTE_TOPIC,0)
	client.publish(mqtt_module.PUB_AUTHENTICATE_TOPIC, decoded_qr);
	time.sleep(5)
	client.disconnect()
	client.loop_stop()
	return HttpResponse(mqtt_module.RESPONSE)
	


