from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from Tasks.services import  LoginService, SignUpService
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BostonAppWS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^$', RedirectView.as_view(url='/user')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^session$', LoginService.as_view()),
    url(r'^user$', SignUpService.as_view())
)
