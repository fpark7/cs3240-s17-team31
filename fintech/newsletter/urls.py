from django.conf.urls import *
from newsletter import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ url(r'^reports/new_report', views.newReport, name='newReport'),
                url(r'^reports/', views.viewReports , name='viewReport')]


