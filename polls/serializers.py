from django.forms import widgets
from rest_framework import serializers
from .models import Poll, Choice

class PollSerializer(serializers.HyperlinkedModelSerializer):
    poll = serializers.HyperlinkedRelatedField(many=True, view_name='poll-detail')

    class Meta:
        model = Poll
        fields = ('question', 'pub_date')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Choice
        fields = ('poll', 'choice_text', 'votes')

# votes = serializers.Field(source='votes')
"""
##### SERIALIZERS #####
class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('url', 'poll', 'text')
        read_only_fields = ('poll',)


class PollSerializer(serializers.HyperlinkedModelSerializer):
    choices = serializers.ManyHyperlinkedRelatedField(
        source = 'choice_set',
        view_name = 'choice-detail',
        read_only = True
    )

    class Meta:
        model = Poll
        fields = ('url', 'name', 'question', 'choices')


class VoteSerializer(serializers.HyperlinkedModelSerializer):
#    choices = serializers.HyperlinkedIdentityField(
#        view_name = 'poll-choice-list',
#        pk_url_kwarg = 'poll_id'
#    )

    class Meta:
        model = Vote
        fields = ('url', 'choices')






class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text """