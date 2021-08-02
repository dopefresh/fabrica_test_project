from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import User, Quiz, Question, Choice
from .serializers import UserSerializer, QuizSerializer, QuestionSerializer, ChoiceSerializer

from loguru import logger
import datetime

class QuizzesView(APIView):
    permission_classes = []    

    def get(self, request):
        try:
            today_datetime = datetime.datetime.now(datetime.timezone.utc)
            today = today_datetime.strftime('%Y-%m-%d')
            quizzes = Quiz.objects.filter(end_date__gte=today)
            quiz_serializer = QuizSerializer(quizzes, many=True)
            return Response(quiz_serializer.data)
        except Exception as e:
            logger.error(str(e))
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class QuizView(APIView):
    permission_classes = []    

    def get(self, request, pk):
        try:
            quiz = Quiz.objects.get(id=pk)
            quiz_serializer = QuizSerializer(quiz, many=False)
            return Response(quiz_serializer.data)
        except Exception as e:
            logger.error(str(e))
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class QuestionView(APIView):
    permission_classes = []    

    def post(self, request, quiz_pk, question_pk):
        try:
            data = request.data
            question = Question.objects.get(pk=question_pk)
            quiz = question.quiz
            
            user, created = User.objects.get_or_create(id=data['user_id'])
            user.quiz_set.add(quiz)
            question = Question.objects.get(pk=question_pk, quiz=quiz)
            for answer in data.get('answers'):
                Choice.objects.update_or_create(
                    answer=answer, 
                    user=User.objects.get(id=data['user_id']), 
                    question=question
                )
                logger.info('Before error')
            return Response('', status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(str(e))
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = QuizSerializer(user.quiz_set.all(), many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(str(e))
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class UserQuestionChoiceView(APIView):
    permission_classes = []

    def get(self, request, user_pk, question_pk):
        try:
            user = User.objects.get(id=user_pk)
            choices = Choice.objects.filter(question__pk=question_pk, user=user)
            serializer = ChoiceSerializer(choices, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(str(e))
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
