from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from newsletter import views as newsletter_views
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

]
