from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

from Tasks.userservices import  LoginService, SignUpService
from Tasks.taskservices import TaskListService
from Tasks.executionservices import ExecutionListService, ExecutionItemService

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BostonAppWS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^$', RedirectView.as_view(url='/user')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^session$', LoginService.as_view()),
    url(r'^user$', SignUpService.as_view()),
    url(r'^tasks/$', TaskListService.as_view()),
    url(r'^executions/$', ExecutionListService.as_view()),
    url(r'^executions/(?P<execution_id>\d+)$', ExecutionItemService.as_view())
)
