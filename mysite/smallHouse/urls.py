from django.conf.urls import url
from . import views

urlpatterns = [
    url('main', views.mainView, name='mainView'),
    url('getAddress', views.getAddress, name='getAddress'),
    url('getBusStop', views.getBusStop, name='getBusStop')
]