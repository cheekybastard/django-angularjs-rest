from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_angularjs_rest.views.home', name='home'),
    # url(r'^django_angularjs_rest/', include('django_angularjs_rest.foo.urls')),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
