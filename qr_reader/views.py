from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
	return HttpResponse("<h2>QR_Reader loads here</h2>")

def read(request):
	# this loads the view inside templates folder inside this app
	# but django treats all the templates folder of different apps as one single /templates folder
	# so it will be wise to namespace them according to the app to remove any possibility of conflict 
	return render(request,"qr_reader/waste_bin.html")

def mqtt_ajax(request):
	decoded_qr =  HttpResponse(request.POST.get("code","error getting code"))