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
        blank=True
    )
    
    class Meta:
        db_table = 'quiz'
        verbose_name_plural = "quizzes"

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
        default=1
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
        verbose_name_plural = "questions"

    def __str__(self):
        return f'title: {self.title}, quiz: {self.quiz.title}'


class Choice(models.Model):
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
        on_delete=models.CASCADE
    )
    
    class Meta:
        db_table = 'choice'
        verbose_name_plural = "choices"
    
    def __str__(self):
        return f'{self.question.title} - {self.answer}'