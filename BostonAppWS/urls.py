from django.conf.urls import patterns, include, url
from Tasks.services import  LoginService, SignUpService
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BostonAppWS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^session$', LoginService.as_view()),
    url(r'^user$', SignUpService.as_view())
)
