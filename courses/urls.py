from django.conf.urls import patterns, include, url
from courses.views import (CoursesListView, CoursesView,
                           CoursesCreate, CoursesUpdate,
                           CoursesDelete)


urlpatterns = patterns('',

    url(r'^$', CoursesListView.as_view(), name='Course_list'),
    url(r'^(?P<pk>\d+)/$', CoursesView.as_view(), name='Course_item'),
    url(r'^add/$', CoursesCreate.as_view(), name='course_add'),
    url(r'^edit/(?P<pk>\d+)/$', CoursesUpdate.as_view(), name='courses_edit'),
    url(r'^del/(?P<pk>\d+)/$', CoursesDelete.as_view(), name='courses_del'),
)
