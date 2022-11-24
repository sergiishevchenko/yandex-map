# Проект where_to_go - Яндекс.Афиша


## Настройка и запуск

Для успешного запуска необходимо указать переменные окружения в файле `.env` в корне проекта.

**Формат `.env` файла:**

ENV=.env

# General Django vars
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=

# Media & static files
MEDIA_URL=/media/
STATIC_URL=/static/

# Как запустить проект локально?
git clone <SSH address of this repo>
cd blog/
python3 -m myenv venv
source venv\bin\activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver

### Деплой
Вы можете посмотреть задеплоенный проект по ссылке - .