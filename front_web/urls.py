__author__ = 'liushuman'

from django.conf.urls import include, url
from front_web import views

urlpatterns = [
    url(r'^test$', views.test, name=''),

    url(r'^$', views.demo_index, name=''),

    url(r'^zillia$', views.index, name='')
]