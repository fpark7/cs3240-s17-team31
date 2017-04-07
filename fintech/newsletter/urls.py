from django.conf.urls import *
from newsletter import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ url(r'^new_report/$', views.newReport, name='newReport'),
                url(r'^new_report/view_report/$', views.viewReports , name='viewReport')]


