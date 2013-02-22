Basic draft notes for rewrite.

Follow on to the django-rest-framework tutorial, use tut browserable snippets api for AngularJS client demo.

# project root urls.py

change from:
 url(r'^', include('snippets.urls')),
 to
 url(r'^api/', include('snippets.urls')),


 # snippets.urls

 To enable .json suffix

 add:
 from rest_framework.urlpatterns import format_suffix_patterns

 change:
 urlpatterns = patterns('snippets.views',

 to:

 urlpatterns = format_suffix_patterns(patterns('snippets.views',
    blahblah
    etc...
    )

 # settings.py

 To enable .json suffix ensure JSONRenderer enabled, aka;
 'rest_framework.renderers.JSONRenderer',

add to:

 REST_FRAMEWORK = {
     'DEFAULT_RENDERER_CLASSES': (
         'rest_framework.renderers.JSONRenderer',
         'rest_framework.renderers.BrowsableAPIRenderer',
     ),
     #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
     #'PAGINATE_BY': 10
 }