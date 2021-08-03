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


