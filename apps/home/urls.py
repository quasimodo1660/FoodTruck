from django.conf.urls import url

from . import views     

urlpatterns = [
    url(r'^$', views.index),  
    url(r'location/(?P<lon>-?[0-9]\d*(\.\d+)?)/(?P<lat>-?[0-9]\d*(\.\d+)?)', views.loc),   
]