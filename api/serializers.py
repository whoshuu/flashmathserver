from api.models import Question, Quiz
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.RelatedField(many=True, source='question_set')
    class Meta:
        model = Quiz
        fields = ('id', 'created', 'questions')
        depth = 2


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'created', 'text', 'answer')
