from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^signup$', views.signup),
    url(r'^profile$', views.show),
]