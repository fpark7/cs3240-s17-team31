from django.conf.urls import *
from sitemanager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                url(r'^$', views.viewSiteManager, name='sm_panel'),
                # url(r'^delete_message/(?P<message_id>\w+)/$', views.delete, name='del'),
                url(r'sm_confirm/', views.smConfirm, name='sm_confirm'),
                url(r'manageGroups/$', views.manageGroups, name='manageGroups'),
                url(r'manageGroups/groupSettings/(?P<group_id>\w+)/$', views.groupSettings, name='groupSettings'),
                url(r'manageReports/$', views.manageReports, name='manageReports'),
                url(r'manageReports/reportSettings/(?P<report_id>\w+)/$', views.reportSettings, name='reportSettings'),
                url(r'manageReports/fileSettings/(?P<report_id>\w+)/$', views.fileSettings, name='fileSettings'),
                ]