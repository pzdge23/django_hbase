from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^year/', views.Year.as_view(), name='year'),
    url(r'^month/', views.Month.as_view(), name='month'),
    url(r'^date/', views.Date.as_view(), name='date'),
]
