from django.db import models
import datetime
from django.utils import timezone

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
    poll = models.ForeignKey(Poll, related_name='voting')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text
"""
##### MODELS #####
class Poll(models.Model):
    question = models.CharField(max_length=200)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.text


class Vote(models.Model):
    user = models.ForeignKey(User)
    poll = models.ForeignKey(Poll)
    choices = models.ManyToManyField(Choice)
"""