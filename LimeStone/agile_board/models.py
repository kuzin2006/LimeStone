from django.db import models
from django.forms import ModelForm


class AgileCard(models.Model):
    TODO = 'TODO'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
    POSSIBLE_STATES = [(TODO, 'TO DO'),
                       (IN_PROGRESS, 'In Progress'),
                       (DONE, 'Done')
                       ]
    modified_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    state = models.CharField(choices=POSSIBLE_STATES, max_length=20)
    active = models.BooleanField(default=True)  # Delete - mark as inactive

    def __str__(self):
        return self.state


class AgileCardForm(ModelForm):
    class Meta:
        model = AgileCard
        fields = ['content', 'state']


