from django.conf.urls import patterns, include, url
#from polls import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_angularjs_rest.views.home', name='home'),
    # url(r'^django_angularjs_rest/', include('django_angularjs_rest.foo.urls')),
     url(r'^polls/', include('polls.urls', namespace="polls")),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     #url(r'^', include('quickstart.urls')),
     url(r'^api/', include('snippets.urls')),
)

"""
if is_installed('api'):
    from api import api
    api.autodiscover()

    urlpatterns += patterns('',
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
        url(r'^api/', include(api.urls)),)
"""