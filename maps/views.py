from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	lat = request.GET.get('lat','default')
	lon = request.GET.get('lon','default')
	clat = request.GET.get('clat','default')
	clon = request.GET.get('clon','default')
	percent_filled = request.GET.get('percent_filled','0')
	exchange = request.GET.get('exchange','0')
	data = {'lat':lat,'lon':lon,'clat':clat,'clon':clon,'percent_filled':percent_filled, 'eur_exchange': exchange}
	return render(request,"maps/index.html",data)
