from fda import views
from django.conf.urls import *

urlpatterns = [
                url(r'^$', views.fdaLogin, name='fda_login'),
                url(r'^getReportsList/', views.getReportsList, name='fda_getReportsList'),

                ]