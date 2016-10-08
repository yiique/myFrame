__author__ = 'liushuman'

from django.conf.urls import include, url
from front_web import views

urlpatterns = [
    url(r'^$', views.demo_index, name=''),

    url(r'^zillia$', views.index, name=''),

    url(r'^paper_lists$', views.paper_lists, name=''),
    url(r'^paper_detail/(.+)$', views.paper_detail, name=''),
    url(r'^paper_edit/(.+)$', views.paper_edit, name=''),
    url(r'^submit_paper_edit/(.+)$', views.submit_paper_edit, name=''),
]