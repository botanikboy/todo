'''
TODO
1. Создание записи /api/record/create - POST
2. Чтение записи /api/record/get?uuid={string} - GET
3. Список записей /api/records/all - GET
4. Список записей на указанные даты
/api/records/list?start={DD.MM.YY}&end={DD.MM.YY} - GET
5. Удаление записи /api/record/delete?uuid={string} - DELETE
'''

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CreateTask, ListTask, DeleteTask, RetriveTask

API_VERSION = ''

router = SimpleRouter()
router.register('record/create', CreateTask)
router.register('records/all', ListTask)
router.register('records/list', ListTask)

urlpatterns = [
    path(f'{API_VERSION}', include(router.urls)),
    path(f'{API_VERSION}record/delete', DeleteTask.as_view()),
    path(f'{API_VERSION}record/get', RetriveTask.as_view()),
]
