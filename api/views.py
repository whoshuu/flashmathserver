from api.models import Question, Quiz
from api.serializers import QuestionSerializer, QuizSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random


class QuizList(APIView):
    def get(self, request, format=None):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)


    def post(self, request, format=None, *args, **kwargs):
        subject = self.kwargs['subject']
        if subject == 'fractions':
            quiz = Quiz(subject='fractions')
            quiz.save()
            for i in range(10):
                multiplier = random.randint(2,9)
                numerator = random.randint(1, 25)
                denom = random.randint(numerator + 1, numerator + 25)
                ans_denom = denom * multiplier
                answer = numerator * multiplier
                text = str(numerator) + '/' + str(denom) + ' is equal to @_@ /' + str(ans_denom)
                question = Question(text=text, answer=str(answer), quiz=quiz)
                question.save()
                quiz.save()
            serializer = QuizSerializer(quiz)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class QuestionList(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    def get_question(self, pk, format=None):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_question(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        question = self.get_question(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
