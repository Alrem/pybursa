from django.conf.urls import patterns, include, url
from coaches.views import coaches_list, coaches_item, coaches_edit, coaches_add


urlpatterns = patterns('',

    url(r'^$', coaches_list, name='Coach_list'),
    url(r'^(?P<coaches_id>\d+)/$', coaches_item, name='Coach_item'),
    url(r'^add$', coaches_add, name='coach_add'),
    url(r'^edit/(?P<coaches_id>\d+)/$', coaches_edit, name='coaches_edit'),
)
