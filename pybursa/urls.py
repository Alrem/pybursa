from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^address/', include('address.urls')),
    url(r'^dossier/', include('dossier.urls')),
    url(r'^$', TemplateView.as_view(template_name='main.html'), name='Home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)