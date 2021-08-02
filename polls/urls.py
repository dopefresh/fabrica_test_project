from django.urls import path

from polls import views

app_name = 'polls'

urlpatterns = [
    path('quizzes/', views.QuizzesView.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>/', views.QuizView.as_view(), name='quiz'),
    path('quizzes/<int:quiz_pk>/<int:question_pk>/', views.QuestionView.as_view(), name='question-answer'),
    path('users/<int:pk>/', views.UserView.as_view(), name='user-quizzes'),
    path('users/<int:user_pk>/<int:question_pk>/', views.UserQuestionChoiceView.as_view(), name='user-quiz-question-answers'),
]
