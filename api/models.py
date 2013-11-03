from django.db import models

class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length='300')
    answer = models.CharField(max_length='25')

    class Meta:
        ordering = ('created',)
