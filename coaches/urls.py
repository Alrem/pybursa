from django.conf.urls import patterns, include, url
from coaches.views import ( CoachesListView, CoachesCreate,
                            CoachesUpdate, CoachesView, CoachesDelete)


urlpatterns = patterns('',

    url(r'^$', CoachesListView.as_view(), name='Coach_list'),
    url(r'^(?P<pk>\d+)/$', CoachesView.as_view(), name='Coach_item'),
    url(r'^add$', CoachesCreate.as_view(), name='coach_add'),
    url(r'^edit/(?P<pk>\d+)/$', CoachesUpdate.as_view(), name='coaches_edit'),
    url(r'^del/(?P<pk>\d+)/$', CoachesDelete.as_view(), name='coaches_remove'),
)
