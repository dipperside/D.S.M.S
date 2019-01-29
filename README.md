# D.S.M.S. - система управления сайтами на django 2

Python >= 3.7

Django >= 2

Postgres == 10

**Установка**
- Форкнуть проект

- Создать файл local_settings.py и прописать

```
from .settings import *

SECRET_KEY = 'ddfdrrt545*^g*&76r*B8f^5e64d9y&()HJ0yu97T&%%7t'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'название БД',
        'USER': 'ваш пользователь',
        'PASSWORD': 'ваш пароль',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SITE_ID = 1
```

- pip install -r req.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


## План

1) App "auth"
2) App "Тарифный план" - какие функции доступны
3) Своя админка для каждого сайта
4) Возможность запуска нового проекта пользователем
5) Скрипт авто уст.
6) Создание проекта через web

## Идеи

1) Две БД. Одна общая, вторая для конкретного проекта
2) Свои apps на каждый проект

