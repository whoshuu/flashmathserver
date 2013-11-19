from django.db import models


class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length='200')

    class Meta:
        ordering = ('created',)


class Quiz(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length='100')

    class Meta:
        ordering = ('created',)


class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length='300')
    answer = models.CharField(max_length='25')
    explanation = models.CharField(max_length='300')
    quiz = models.ForeignKey(Quiz)

    class Meta:
        ordering = ('created',)


class Score(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length='100')
    value = models.SmallIntegerField()
    student = models.ForeignKey(Student)

    class Meta:
        ordering = ('created', )
