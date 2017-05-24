"""sgb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^qr_reader$', views.qr_reader, name="qr_reader"),
    url(r'^qr_reader_sabin$', views.qr_reader_sabin, name="qr_reader_sabin"),
    url(r'^ajax$', views.mqtt_ajax_authenticate, name="mqtt-ajax-authenticate"),
    url(r'^waste$', views.mqtt_ajax_waste, name="mqtt-ajax-waste"),
    url(r'^qr_reader_custom$', views.custom_waste_bin, name="qr_reader_custom")
]
