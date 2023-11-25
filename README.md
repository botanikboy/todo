# ToDo список дел api сервис
Простой api сервис для списка дел.

## Установка

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Если всё прошло успешно проект доступен по адресу, описание API:
http://localhost/

Доступные эндпоинты:
1. Создание записи /api/record/create - POST
2. Чтение записи /api/record/get?uuid={string} - GET
3. Список записей /api/records/all - GET
4. Список записей на указанные даты
/api/records/list?start={DD.MM.YY}&end={DD.MM.YY} - GET
5. Удаление записи /api/record/delete?uuid={string} - DELETE

## Основные технологии
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)

## Об авторе
Разработано:
[Илья Савинкин](https://www.linkedin.com/in/ilya-savinkin-6002a711/)
