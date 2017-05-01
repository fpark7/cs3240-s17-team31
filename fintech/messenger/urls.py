from django.conf.urls import *
from messenger import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ url(r'^new_message/', views.newMessage, name='newMessage'),
                url(r'^$', views.viewMessages, name='inbox'),
                url(r'^delete_message/(?P<message_id>\d+)/$', views.delete, name='del'),
                url(r'^unencrypt_message/(?P<message_id>\d+)/$', views.unencrypt, name='une'),
                url(r'^groupEmail/', views.groupEmail, name='groupEmail'),
                ]
