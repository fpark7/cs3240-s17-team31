from django.conf.urls import *
from search import views

urlpatterns = [ url(r'^$', views.newSearch, name='search'),
                url(r'^view_search/', views.viewSearch, name='viewSearch')]
