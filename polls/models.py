from django.db import models

from datetime import date
from loguru import logger


CHOICE_TYPE = (
    ('Text', 'Ответ текстом'),
    ('Choice', 'Выбор варианта'),
    ('Choices', 'Выбор нескольких вариантов')
)


class User(models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = "Пользователи"


class Quiz(models.Model):
    """
    Модель опроса
    """
    title = models.CharField(max_length=70, blank=False, null=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=False, null=False, default=date.today)
    description = models.TextField()
    users = models.ManyToManyField(
        User, 
        blank=True,
        related_name='quizzes'
    )
    
    class Meta:
        db_table = 'quiz'
        verbose_name_plural = "Опросы"

    def save(self, *args, **kwargs):
        logger.info(kwargs)
        if self.id is None:
            super().save(*args, **kwargs)
        else:
            prev_state = Quiz.objects.get(id=self.id)
            self.start_date = prev_state.start_date
            super().save(*args, **kwargs)

    def __str__(self):
        return f'title: {self.title}, start date: {self.start_date}'
        

class Question(models.Model):
    """
    Модель вопроса
    """
    quiz = models.ForeignKey(
        Quiz, 
        on_delete=models.CASCADE,
        default=1,
        related_name='questions'
    )
    title = models.CharField(
        max_length=200, 
        blank=False, 
        null=False, 
        default=''
    )
    choice_type = models.CharField(
        choices=CHOICE_TYPE, 
        max_length=20, 
        blank=False, 
        null=False, 
        default='Text'
    )
    
    class Meta:
        db_table = 'question'
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f'title: {self.title}, quiz: {self.quiz.title}'


class AvailableChoice(models.Model):
    """
    Модель доступного пользователю ответа 
    """
    answer = models.TextField(blank=False, null=False, default='')
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE,
        related_name='available_choices'
    )
    class Meta:
        db_table = 'available_choice'
        verbose_name_plural = "Доступные пользователю выборы"
    
    def __str__(self):
        return f'{self.question.title} - {self.answer}'


class UserChoice(models.Model):
    """
    Модель ответа пользователя
    """
    answer = models.TextField(blank=False, null=False, default='')
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        default=None,
        blank=True, null=True
    )
    question = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE,
        related_name='user_choices'
    )
    
    class Meta:
        db_table = 'user_choice'
        verbose_name_plural = "Выборы пользователя"
    
    def __str__(self):
        return f'{self.question.title} - {self.answer}'

