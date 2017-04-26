from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from newsletter import views as newsletter_views
from newsfeed import views as newsfeed_views
from django.conf.urls.static import static
from django.conf import settings

# from messenger import views as message_views

urlpatterns = [
    # Examples:
    url(r'^$', newsletter_views.register, name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^signup/', newsletter_views.register, name='signup'), # name used for HTML <a> tag
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^invalid/', newsletter_views.invalid),
    url(r'^logout/', auth_views.logout, name='logout'),
    url(r'^home/', newsletter_views.homeView, name='home'),
    url(r'^newgroup/',newsletter_views.newGroup,name='newgroup'),
    url(r'^invalidGroup/', newsletter_views.invalidGroup),
    url(r'^groups/', newsletter_views.viewGroups, name='groups'),
    url(r'^viewgroup/(?P<group_id>\d+)/$',newsletter_views.viewGroup,name='group'),
    url(r'^inbox/', include('messenger.urls'), name='inbox'),
    url(r'^sm_panel/', include('sitemanager.urls'), name='sm_panel'),
    url(r'^search/', include('search.urls'), name='search'),
    url(r'^fda/', include('fda.urls')),

    #url(r'^feed/', newsfeed_views.feed, name='feed'),

    ### don't touch anything under here ###
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
