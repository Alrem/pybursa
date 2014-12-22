from django.conf.urls import patterns, include, url
from courses.views import courses_list, courses_item, courses_edit, courses_add


urlpatterns = patterns('',

    url(r'^$', courses_list, name='Course_list'),
    url(r'^(?P<courses_id>\d+)/$', courses_item, name='Course_item'),
    url(r'^add/$', courses_add, name='course_add'),
    url(r'^edit/(?P<courses_id>\d+)/$', courses_edit, name='courses_edit'),
)
