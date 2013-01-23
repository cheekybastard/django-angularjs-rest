from django.forms import widgets
from rest_framework import serializers
from polls import models

class PollSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    question = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance
            instance.question = attrs['question']
            instance.pub_date = attrs['pub_date']
            return instance

        # Create new instance
        return models.Poll(**attrs)

class ChoiceSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    choice_text = serializers.CharField(max_length=200)
    votes = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance
            instance.choice_text = attrs['choice_text']
            instance.votes = attrs['votes']
            return instance

        # Create new instance
        return models.Choice(**attrs)

"""class Poll(models.Model):
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