from api.models import Question
from api.serializers import QuestionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
