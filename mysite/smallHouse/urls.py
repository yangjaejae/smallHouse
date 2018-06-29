from django.conf.urls import url
from . import views

urlpatterns = [
    url('main', views.mainView, name='mainView'),
    url('getAddr', views.getAddr, name='getAddress')
]