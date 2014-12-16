from django.conf.urls import patterns, include, url
from address.views import address_list, address_item


urlpatterns = patterns('',

    url(r'^$', address_list, name='Address_list'),
    url(r'^(?P<address_id>\d+)/$', address_item, name='address_item'),

)
