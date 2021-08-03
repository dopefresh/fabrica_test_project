from rest_framework import serializers

from .models import User, Quiz, Question, UserChoice


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(many=False, read_only=True)

    class Meta:
        model = Question
        fields = ('quiz', 'title', 'choice_type',)


class UserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoice
        fields = ('answer', 'question',)



class ManyUserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoice
        fields = ('answer',)


class ManyQuestionSerializer(serializers.ModelSerializer):
    user_choices = UserChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('title', 'choice_type', 'user_choices',)


class QuizQuestionAnswersSerializer(serializers.ModelSerializer):
    questions = ManyQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('title', 'start_date', 'end_date', 'questions',)


class UserQuizQuestionAnswersSerializer(serializers.ModelSerializer):
    quizzes = QuizQuestionAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'quizzes',)

