from django.conf.urls import patterns, include, url
from contacts.views import CreateMessage


urlpatterns = patterns('',

    url(r'^$', CreateMessage.as_view(), name='Contacts'),

)
