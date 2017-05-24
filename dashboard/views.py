from django.shortcuts import render
from django.http import HttpResponse
import urllib2
import json

# Create your views here.

def index(request):
	try:
	 	response = urllib2.urlopen('http://localhost:3000/api/account')
	 	data = json.load(response)
	 	return render(request,"dashboard/dashboard.html",data)
	except urllib2.HTTPError, e:
	    print e.code
	    return HttpResponse("<h2>Invalid API url</h2>")
	except urllib2.URLError, e:
	    print e.args
	    return HttpResponse("<h2>Invalid API url</h2>")
	


def accounts(request):
	return render(request,"dashboard/user.html")	
