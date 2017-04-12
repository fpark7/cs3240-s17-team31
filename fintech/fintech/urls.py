from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from newsletter import views as newsletter_views
from messenger import views as message_views

urlpatterns = [
    # Examples:
     url(r'^$', newsletter_views.register, name='index'),
     #url(r'^$', message_views.register, name='create'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^signup/', newsletter_views.register, name='signup'), # name used for HTML <a> tag
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^invalid/', newsletter_views.invalid),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^home/', newsletter_views.homeView, name='home'),
    url(r'^newgroup/',newsletter_views.makeGroup,name='group'),

    # url(r'^signup/', message_views.register, name='create'),
    url(r'^inbox/', include('messenger.urls')),
]
