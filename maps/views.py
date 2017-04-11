from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	lat = request.GET.get('lat','default')
	lon = request.GET.get('lon','default')
	clat = request.GET.get('clat','default')
	clon = request.GET.get('clon','default')
	percent_filled = request.GET.get('percent_filled','default')
	return render(request,"maps/index.html",{'lat':lat,'lon':lon,'clat':clat,'clon':clon,'percent_filled':percent_filled})
