from django.conf.urls import include, url
from django.contrib import admin
from newsletter import views as newsletter_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'fintech.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^signup/', newsletter_views.signupform),
    url(r'^admin/', include(admin.site.urls)),
]
