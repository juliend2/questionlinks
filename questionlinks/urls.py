from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('questionlink_django.questionlinks.views',
	(r'^$', 'questions'),
	(r'^questions/$', 'questions'),
	(r'^register/$', 'register'),
	(r'^login/$', 'login'),
	(r'^logout/$', 'logout'),	
	(r'^delete_question/(?P<id>\d+)/$', 'delete_question'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
	)
