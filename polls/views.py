from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import AvailableChoice, User, Quiz, Question, UserChoice
from .serializers import UserSerializer, QuizSerializer, QuestionSerializer, UserChoiceSerializer, UserQuizQuestionAnswersSerializer

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
            questions = Question.objects.filter(quiz__pk=pk)
            question_serializer = QuestionSerializer(questions, many=True)
            return Response(question_serializer.data)
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
            user.quizzes.add(quiz)
            question = Question.objects.get(pk=question_pk, quiz=quiz)
            question.user_choices.all().delete()
            
            if question.choice_type == 'Choices' or question.choice_type == 'Choice':
                available_choices = AvailableChoice.objects.filter(question=question)
                available_choices = [choice.answer for choice in available_choices] 
                choices = []
                for answer in data.get('answers'):
                    if answer not in available_choices:
                        return Response('Not available choice', status=status.HTTP_400_BAD_REQUEST)

                    choice = UserChoice(
                        answer=answer, 
                        user=User.objects.get(id=data['user_id']), 
                        question=question
                    )
                    choices.append(choice)
                if not len(choices):
                    return Response('No choice provided', status=status.HTTP_400_BAD_REQUEST)
                
                if question.choice_type == 'Choices':     
                    UserChoice.objects.bulk_create(choices)
                    return Response('', status=status.HTTP_201_CREATED)
                
                if len(choices) > 1:
                    return Response('Too many choices', status=status.HTTP_400_BAD_REQUEST)
                choices[0].save()
                
                return Response('', status=status.HTTP_201_CREATED)

            choices = []
            for answer in data.get('answers'):
                logger.info("Before error 2")
                choice = UserChoice(
                    answer=answer, 
                    user=User.objects.get(id=data['user_id']), 
                    question=question
                )
                choices.append(choice)
            if not len(choices):
                return Response('No choice provided', status=status.HTTP_400_BAD_REQUEST)
            if len(choices) > 1:
                return Response('Too many choices', status=status.HTTP_400_BAD_REQUEST)

            logger.info('Before error 3')
            choices[0].save()
            return Response('', status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(str(e))
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = []

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            logger.info(user)
            serializer = UserQuizQuestionAnswersSerializer(instance=user, many=False)
            logger.info(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            logger.error(str(e))
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
