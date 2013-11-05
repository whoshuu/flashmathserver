from api.models import Question, Quiz, Score
from api.serializers import QuestionSerializer, QuizSerializer, ScoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random


class ScoreList(APIView):
    def get(self, request, format=None):
        scores = Score.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)


class ScoreSubjectList(APIView):
    def get(self, request, subject, format=None):
        scores = Score.objects.all().filter(subject=subject)
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)


class ScorePost(APIView):
    def get(self, request, subject, value, format=None):
        score = Score(subject=subject, value=value)
        score.save()
        scores = Score.objects.all().filter(subject=subject)
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizList(APIView):
    def get(self, request, format=None):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)


class FractionQuiz(APIView):
    def get(self, request, format=None):
        quiz = Quiz(subject='fractions')
        quiz.save()
        for i in range(10):
            multiplier = random.randint(2, 9)
            numerator = random.randint(1, 25)
            denom = random.randint(numerator + 1, numerator + 25)
            ans_denom = denom * multiplier
            answer = numerator * multiplier
            text = str(numerator), str(denom), str(ans_denom)
            explanation = 'The correct answer is ' + str(answer) + ' because ' + str(numerator) + '/' + str(denom) + ' times ' + str(multiplier) + '/' + str(multiplier) + ' is ' + str(answer) + '/' + str(ans_denom)
            question = Question(text=text, answer=str(answer), explanation=explanation, quiz=quiz)
            question.save()
            quiz.save()
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)


class MultiplicationQuiz(APIView):
    def get(self, request, format=None):
        quiz = Quiz(subject='multiplication')
        quiz.save()
        for i in range(10):
            x = random.randint(1, 12)
            y = random.randint(1, 12)
            answer = x * y
            text = str(x), str(y)
            explanation = str(x) + ' times ' + str(y) + ' is equal to ' + str(answer)
            question = Question(text=text, answer=str(answer), explanation=explanation, quiz=quiz)
            question.save()
            quiz.save()
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)


class AdditionQuiz(APIView):
    def get(self, request, format=None):
        quiz = Quiz(subject='addition')
        quiz.save()
        for i in range(10):
            x = random.randint(1, 50)
            y = random.randint(1, 50)
            answer = x + y
            text = str(x), str(y)
            explanation = str(x) + ' + ' + str(y) + ' is equal to ' + str(answer)
            question = Question(text=text, answer=str(answer), explanation=explanation, quiz=quiz)
            question.save()
            quiz.save()
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)


class SubtractionQuiz(APIView):
    def get(self, request, format=None):
        quiz = Quiz(subject='subtraction')
        quiz.save()
        for i in range(10):
            x = random.randint(5, 100)
            y = random.randint(1, x - 1)
            answer = x - y
            text = str(x), str(y)
            explanation = str(x) + ' - ' + str(y) + ' is equal to ' + str(answer)
            question = Question(text=text, answer=str(answer), explanation=explanation, quiz=quiz)
            question.save()
            quiz.save()
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)


class DivisionQuiz(APIView):
    def get(self, request, format=None):
        quiz = Quiz(subject='division')
        quiz.save()
        for i in range(10):
            y = random.randint(1, 12)
            answer = random.randint(1, 12)
            x = y * answer
            text = str(x), str(y)
            explanation = str(x) + ' divided by ' + str(y) + ' is equal to ' + str(answer)
            question = Question(text=text, answer=str(answer), explanation=explanation, quiz=quiz)
            question.save()
            quiz.save()
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)


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
