from django.conf.urls import patterns, include, url
from students.views import students_list, students_item, student_edit, student_add


urlpatterns = patterns('',

    url(r'^$', students_list, name='Student_list'),
    url(r'^(?P<student_id>\d+)/$', students_item, name='Student_item'),
    url(r'^add$', student_add, name='student_add'),
    url(r'^edit/(?P<student_id>\d+)/$', student_edit, name='student_edit'),
)
