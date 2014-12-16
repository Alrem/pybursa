from django.conf.urls import patterns, include, url
from dossier.views import dossier_list, dossier_item


urlpatterns = patterns('',

    url(r'^$', dossier_list, name='Dossier_list'),
    url(r'^(?P<dossier_id>\d+)/$', dossier_item, name='dossier-item'),

)
