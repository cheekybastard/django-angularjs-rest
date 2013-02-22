from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from rest_framework import generics
from rest_framework import renderers
from rest_framework import permissions
#from permissions import IsOwnerOrReadOnly
from .serializers import PollSerializer, ChoiceSerializer
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Choice, Poll

class HomeView(TemplateView):
    template_name = 'index.html'

class PollList(generics.ListCreateAPIView):
    """
    list all polls.
    """
    model = Poll
    serializer_class = PollSerializer
    #renderer_classes = (JSONRenderer, JSONPRenderer) <= needs APIView class
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def vote(request, poll_id):
        p = get_object_or_404(Poll, pk=poll_id)
        try:
            selected_choice = p.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the poll voting form.
            return render(request, 'polls/detail.html', {
                'poll': p,
                'error_message': "You didn't select a choice.",
                })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

    #def pre_save(self, obj):
    #    obj.owner = self.request.user

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve results poll instance
    """
    model = Choice
    serializer_class = ChoiceSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                      IsOwnerOrReadOnly,)

    def results(request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        return render(request, 'polls/results.html', {'poll': poll})


    #def pre_save(self, obj):
    #    obj.owner = self.request.user




"""

class ChoiceList(generics.ListCreateAPIView):
    model = Choice
    serializer_class = ChoiceSerializer
#    paginate_by = 10

    def pre_save(self, obj):
        poll_id = self.kwargs.get('poll_id')
        obj.poll = Poll.objects.get(pk=poll_id)

    def get_queryset(self):
        poll_id = self.kwargs.get('poll_id')
        return Choice.objects.filter(poll=poll_id)


class VoteList(generics.ListCreateAPIView):
    model = Vote
    serializer_class = VoteSerializer
    paginate_by = 10

    def pre_save(self, obj):
        obj.user = self.request.user
        poll_id = self.kwargs.get('poll_id')
        obj.poll = Poll.objects.get(pk=poll_id)

    def get_queryset(self):
        user = self.request.user
        poll_id = self.kwargs.get('poll_id')
        return Vote.objects.filter(user=user, poll=poll_id)

# class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('url', 'poll', 'text')
        read_only_fields = ('poll',)









from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import Choice, Poll

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})




from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
"""