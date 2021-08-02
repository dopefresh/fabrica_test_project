## __Административная панель__:
localhost:8000/admin

-----------------------
## __API__:

### GET:
    localhost:8000/api/v1/quizzes/ - Список всех опросов
    localhost:8000/api/v1/quizzes/id/ - Вопросы в опросе с id = id
    localhost:8000/api/v1/users/id/ - Список опросов, которые начал/закончил пользователь с id=id
    localhost:8000/api/v1/users/user_id/question_id - Ответы пользователя на вопрос с id = question_id

### POST:
    localhost:8000/api/v1/quizzes/quiz_id/question_id/ - Создать ответ/ответы на вопрос с question_id = question_id 


# Запуск: 
git clone https://github.com/dopefresh/fabrica_test_project.git
poetry install
poetry shell

Создаём файл .env с содержимым: 
SECRET_KEY='k7)6)$r#e^s5^-4hk9(az(r106xff6fg+-hk%^cz+k&h2&#l%a'

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
