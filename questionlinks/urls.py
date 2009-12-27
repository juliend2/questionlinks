from django.conf.urls.defaults import *

urlpatterns = patterns('questionlink_django.questionlinks.views',
	(r'^register/$', 'register'),
	(r'^questions/$', 'questions'),
	(r'^login/$', 'login'),
	(r'^logout/$', 'logout'),
)