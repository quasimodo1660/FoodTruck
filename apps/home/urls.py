from django.conf.urls import url

from . import views     

urlpatterns = [
    # url(r'^$',views.home,name='home_page'),
    url(r'^$', views.index),  
    url(r'^search/',views.search),
    url(r'^chat/users$',views.chat_users),
    url(r'^chat/',views.chat),
    url(r'^about/',views.about),
]