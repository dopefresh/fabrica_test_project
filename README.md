## __Административная панель__:
localhost:8000/admin

-----------------------
## __API__:

### GET:
    localhost:8000/api/v1/quizzes/ - Список всех опросов
    localhost:8000/api/v1/quizzes/id/ - Вопросы в опросе с id = id
    localhost:8000/api/v1/users/id/ - Список опросов, которые начал/закончил пользователь с id=id

### POST:
    localhost:8000/api/v1/quizzes/quiz_id/question_id/ - Создать ответ/ответы на вопрос с question_id = question_id 
    request body:
    {
        "answers": [
            "Yes",
            "No",
            "LaLa",
            "Another answer"
        ],
        "user_id": 1
    }    

# Запуск: 
1. git clone https://github.com/dopefresh/fabrica_test_project.git
2. curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
2. Если не вышел 2 шаг в PowerShellе вводим:    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python - 
2. Если снова не вышел 2 шаг:  pip install poetry либо pip3 install poetry
3. poetry install
4. poetry shell
5. Создаём файл .env с содержимым: SECRET_KEY='k7)6)$r#e^s5^-4hk9(az(r106xff6fg+-hk%^cz+k&h2&#l%a'
6. в psql вводим: CREATE DATABASE polls_db;
7. python manage.py migrate
8. docker-compose up
