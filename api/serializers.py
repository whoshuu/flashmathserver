from api.models import Question, Quiz
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'created', 'text', 'answer')


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='question_set')
    class Meta:
        model = Quiz
        fields = ('id', 'created', 'subject', 'questions')
