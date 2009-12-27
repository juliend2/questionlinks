from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('questionlinks_django.questionlinks.views',
	(r'^$', 'index'),
	(r'^questions/$', 'questions'),
	(r'^register/$', 'register'),
	(r'^login/$', 'login'),
	(r'^logout/$', 'logout'),	
	(r'^delete_question/(?P<id>\d+)/$', 'delete_question'),
	(r'^add_answer/(?P<question_id>\d+)/$', 'add_answer'),
	(r'^delete_answer/(?P<id>\d+)/$', 'delete_answer'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
	)
