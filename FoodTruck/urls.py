"""FoodTruck URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.users import views as UV
from apps.lunchbox import views as LV
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UV.UserViewSet)
router.register(r'groups', UV.GroupViewSet)
router.register(r'lunchbox',LV.LunchboxViewSet)
router.register(r'review',LV.ReviewViewSet)
router.register(r'images',LV.LunchboxImageViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^',include('apps.home.urls')),
    url(r'^lunchbox/',include('apps.lunchbox.urls')),
    url(r'^accounts/',include('apps.users.urls')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


