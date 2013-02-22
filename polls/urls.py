
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
#from django.views.generic import DetailView, ListView
from .views import PollList, PollDetail

urlpatterns = format_suffix_patterns(patterns('',
                       url(r'^$', PollList.as_view(), name='poll-list'),
                       url(r'^(?P<pk>\d+)/$', PollDetail.as_view(), name='choice-detail'),
                       url(r'^(?P<pk>\d+)/results/$', PollDetail.as_view(), name='choice-detail'),
                       url(r'^(?P<poll_id>\d+)/vote/$', PollDetail.as_view(), name='choice-detail'),
                       ))

#urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

"""
##### URLS #####
urlpatterns = patterns('',
    url(r'^$', poll_root, name='poll-root'),
    url(r'^polls/$', PollList.as_view(), name='poll-list'),
    url(r'^poll/(?P<pk>\d+)/$', PollDetail.as_view(), name='poll-detail'),
    url(r'^choice/(?P<pk>\d+)/$', ChoiceDetail.as_view(), name='choice-detail'),
    url(r'^vote/(?P<pk>\d+)/$', VoteDetail.as_view(), name='vote-detail'),
    url(r'^poll/(?P<poll_id>\d+)/choices/$', ChoiceList.as_view(), name='poll-choice-list'),
    url(r'^poll/(?P<poll_id>\d+)/votes/$', VoteList.as_view(), name='poll-vote-list')
)



urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name='vote'),
)
"""