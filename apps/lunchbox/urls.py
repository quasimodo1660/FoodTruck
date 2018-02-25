from django.conf.urls import url

from . import views     

urlpatterns = [
    url(r'^$', views.index),  
    url(r'^add/', views.add),
    url(r'^update/',views.update),
    url(r'^uplaods/',views.uplaods),
    url(r'^(?P<id>\d+)$', views.show),
    url(r'^angular/(?P<id>\d+)$',views.showAn),
]

