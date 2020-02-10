## Технологии:
* Django
* DRF
* React
* Bootstrap
* Django-cors-headers

## Описание:
Разработка приложения моделирующего работу фильмотеки. Реализация в виде сервиса с API,дополнительно возможно реализация 
на основе этого API клиент-серверного приложения(rest). Где клиент - React, сервер - Django.

## Сущности: 
* Пользователь 
* Фильм

## Описание работы:
На главной странице отображаем список всех пользователей. При нажатии на имя пользователя переходим на страницу со 
списком фильмов, которые смотрел пользователь и его оценка и отзыва на фильм.На вкладке с названием всех фильмов, при 
нажатии на название фильма - переход на страницу со всеми отзывами на этот фильм. На вкладке API можно посмотреть описание
существующего API. Есть возможность регистрации и аутентификации, посещение личного профиля.

## Фичи:
+ [x] Клиент на Django
+ [x] API используя DRF. Описание API можно посмотреть на вкладке API сайта
+ [x] Авторизация через сторонние сервисы.(Facebook, Linkedin). https://webdevblog.ru/django-autentifikaciya-s-facebook-instagram-i-linkedin/
+ [x] Отдельная ветка deploy. На деплой - uWSGI + nginx. https://webdevblog.ru/razvertyvanie-prilozheniya-na-django-s-uwsgi-i-nginx-v-proizvodstvennoj-srede/ 

## Опционально:
+ [ ] Клиент-серверное приложение с использованием React
+ [ ] Покрытие тестами.
+ [x] Простенький Readme.md файл. 
+ [x] Создать fixtures для приложений.
+ [ ] Прикрутить Docker

## Локальная установка
1) python3 -m venv ./env
2) source env/bin/activate
3) pip install -r requirements.txt
4) python manage.py migrate
5) python manage.py createsuperuser
6) python manage.py runserver

## В настройках установить ключи приложения Facebook
SOCIAL_AUTH_FACEBOOK_KEY = 'key'  
SOCIAL_AUTH_FACEBOOK_SECRET = 'app secret'

