from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from newsletter import views as newsletter_views

urlpatterns = [
    # Examples:
     #url(r'^$', views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^signup/', newsletter_views.signupform),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^home/', auth_views.logout, name='logout'),
]
