# Проект where_to_go - Яндекс.Афиша

## Задание
- Создать **Django**-проект;
- Сделать **API** с данными от **Артёма**;
- Сделать админку максимально удобной для заполнения.

## Настройка и запуск
Для успешного запуска необходимо указать переменные окружения в файле `.env` в корне проекта.

## Как запустить проект локально?
```
git clone <SSH address of this repo> \n
cd yandex_map/
python3 -m myenv venv
source venv\bin\activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver
```

## Добавить новую локацию
В командной строке нужно ввести следующую команду
```
python manage.py load_place <json file link>
```

## Деплой
Вы можете посмотреть задеплоенный проект по ссылке - https://serg8989.pythonanywhere.com/places.
