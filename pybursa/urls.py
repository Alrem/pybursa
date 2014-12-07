from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^product/$', TemplateView.as_view(template_name='product.html'), name="product"),
    url(r'^products/$', TemplateView.as_view(template_name='prod.html'), name="prod"),
    url(r'^admin/', include(admin.site.urls)),
)
