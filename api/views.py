from api.models import Question, Quiz, Score, Student
from api.serializers import QuestionSerializer, QuizSerializer, ScoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random

num_questions = 10


def get_student(token):
    try:
        return Student.objects.get(token=token)
    except Student.DoesNotExist:
        return Student.objects.create(token=token)


class NewRelicPing(APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


class ScoreClear(APIView):
    def get(self, request, subject, format=None):
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        scores = Score.objects.all().filter(subject=subject, student=student)
        scores.delete();
        return Response(status=status.HTTP_200_OK)
    

class ScoreList(APIView):
    def get(self, request, format=None):
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        scores = Score.objects.all().filter(student=student)
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)


class ScoreSubjectList(APIView):
    def get(self, request, subject, format=None):
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        scores = Score.objects.all().filter(subject=subject, student=student)
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)


class ScorePost(APIView):
    def get(self, request, subject, value, format=None):
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        score = Score(subject=subject, value=value, student=student)
        score.save()
        scores = Score.objects.all().filter(subject=subject, student=student)
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuizList(APIView):
    def get(self, request, format=None):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)


class FractionQuiz(APIView):
    def get(self, request, format=None):
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        quiz = Quiz(subject='fractions')
        quiz.save()
        scores = Score.objects.all().filter(subject='fractions', student=student)
        avg = 0
        if len(scores) > 2:
            for score in scores:
                avg = avg + score.value
            avg = avg / len(scores)
        if avg <= num_questions / 3.0:
            low_mult = 2
            high_mult = 3
            low_num = 1
            high_num = 3
            high_denom = 6
        elif avg <= (2 * num_questions) / 3.0:
            low_mult = 3
            high_mult = 5
            low_num = 1
            high_num = 4
            high_denom = 8
        else:
            low_mult = 6
            high_mult = 9
            low_num = 1
            high_num = 5
            high_denom = 10
        for i in range(num_questions):
            multiplier = random.randint(low_mult, high_mult)
            numerator = random.randint(low_num, high_num)
            denom = random.randint(numerator + 1, high_denom)
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
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        quiz = Quiz(subject='multiplication')
        quiz.save()
        scores = Score.objects.all().filter(subject='multiplication', student=student)
        avg = 0
        if len(scores) > 2:
            for score in scores:
                avg = avg + score.value
            avg = avg / len(scores)
        if avg <= num_questions / 3.0:
            low = 1
            high = 4
        elif avg <= (2 * num_questions) / 3.0:
            low = 3
            high = 7
        else:
            low = 6
            high = 12
        for i in range(num_questions):
            x = random.randint(low, high)
            y = random.randint(low, high)
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
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        quiz = Quiz(subject='addition')
        quiz.save()
        scores = Score.objects.all().filter(subject='addition', student=student)
        avg = 0
        if len(scores) > 2:
            for score in scores:
                avg = avg + score.value
            avg = avg / len(scores)
        if avg <= num_questions / 3.0:
            low = 1
            high = 9
        elif avg <= (2 * num_questions) / 3.0:
            low = 5
            high = 20
        else:
            low = 15
            high = 99
        for i in range(num_questions):
            x = random.randint(low, high)
            y = random.randint(low, high)
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
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        quiz = Quiz(subject='subtraction')
        quiz.save()
        scores = Score.objects.all().filter(subject='subtraction', student=student)
        avg = 0
        if len(scores) > 2:
            for score in scores:
                avg = avg + score.value
            avg = avg / len(scores)
        if avg <= num_questions / 3.0:
            low_x = 3
            low_y = 1
            high = 9
        elif avg <= (2 * num_questions) / 3.0:
            low_x = 5
            low_y = 3
            high = 20
        else:
            low_x = 15
            low_y = 11
            high = 99
        for i in range(num_questions):
            x = random.randint(low_x, high)
            y = random.randint(low_y, x - 1)
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
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        quiz = Quiz(subject='division')
        quiz.save()
        scores = Score.objects.all().filter(subject='division', student=student)
        avg = 0
        if len(scores) > 2:
            for score in scores:
                avg = avg + score.value
            avg = avg / len(scores)
        if avg <= num_questions / 3.0:
            low = 1
            high = 4
        elif avg <= (2 * num_questions) / 3.0:
            low = 3
            high = 7
        else:
            low = 6
            high = 12
        for i in range(num_questions):
            y = random.randint(low, high)
            answer = random.randint(low, high)
            x = y * answer
            text = str(x), str(y)
            explanation = str(x) + ' divided by ' + str(y) + ' is equal to ' + str(answer)
            question = Question(text=text, answer=str(answer), explanation=explanation, quiz=quiz)
            question.save()
            quiz.save()
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)


class GeometryQuiz(APIView):
    def get(self, request, format=None):
        if not 'token' in request.GET:
            return Response(status=status.HTTP_404_NOT_FOUND)
        student = get_student(request.GET['token'])
        quiz = Quiz(subject='geometry')
        quiz.save()
        area = random.choice(['Area', 'Perimeter'])
        scores = Score.objects.all().filter(subject='geometry', student=student)
        avg = 0
        if len(scores) > 2:
            for score in scores:
                avg = avg + score.value
            avg = avg / len(scores)
        if avg <= num_questions / 3.0:
            shape = 'Square'
            low = 2
            high = 5
        elif avg <= (2 * num_questions) / 3.0:
            shape = random.choice(['Square', 'Rectangle'])
            low = 3
            high = 9
        else:
            shape = random.choice(['Square', 'Rectangle', 'Triangle'])
            low = 6
            high = 20
        for i in range(num_questions):
            val = ''
            if shape == 'Square':
                x = random.randint(low, high)
                if area == 'Area':
                    answer = x * x
                elif area == 'Perimeter':
                    answer = 4 * x
                val = str(x)
            elif shape == 'Rectangle':
                x = random.randint(low, high)
                y = random.randint(low, high)
                if area == 'Area':
                    answer = x * y
                elif area == 'Perimeter':
                    answer = 2 * (x + y)
                val = str(x) + ' ' + str(y)
            elif shape == 'Triangle':
                x = random.randint(low, high)
                y = random.randint(low, high)
                while y == x:
                    y == random.randint(low, high)
                if area == 'Area':
                    answer = x * y
                    if y > x:
                        val = str(x) + ' ' + str(y)
                    else:
                        val = str(y) + ' ' + str(x)
                elif area == 'Perimeter':
                    pythag = random.choice([[3, 4, 5],
                                            [5, 12, 13],
                                            [8, 15, 17],
                                            [7, 24, 25],
                                            [9, 40, 41],
                                            [11, 60, 61],
                                            [12, 35, 37],
                                            [16, 63, 65],
                                            [20, 21, 29]])
                    answer = pythag[0] + pythag[1] + pythag[2]
                    val = str(pythag[0]) + ' ' + str(pythag[1]) + ' ' + str(pythag[2])
            text = shape, area, val
            explanation = 'blank on purpose'
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
