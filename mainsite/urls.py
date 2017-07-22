from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.base),
    url(r'^aboutus', views.aboutus),
    url(r'^ourteam', views.ourteam),
]