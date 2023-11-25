import datetime as dt

from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from todo_list.models import Task
from .serializers import TaskSerialiser
from .core import UuidGenerator


class CreateTask(GenericViewSet, generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser

    def perform_create(self, serializer):
        if serializer.is_valid():
            generator = UuidGenerator()
            uuid = generator.generate()
            serializer.save(uuid=uuid)


class ListTask(GenericViewSet, generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser
    filter_backends = [DjangoFilterBackend, ]

    def get_queryset(self):
        start_str = self.request.query_params.get('start')
        end_str = self.request.query_params.get('end')
        if all([start_str is not None,
               end_str is not None]):
            start_date = dt.datetime.strptime(start_str, '%d.%m.%y')
            end_date = (dt.datetime.strptime(end_str, '%d.%m.%y')
                        + dt.timedelta(hours=23, minutes=59, seconds=59))
            return self.queryset.filter(created__range=(start_date, end_date))
        else:
            return self.queryset


class RetriveTask(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TaskSerialiser

    def get_object(self):
        uuid = self.request.query_params.get('uuid')
        if uuid is not None:
            task = get_object_or_404(Task, uuid=uuid)
            return task


class DeleteTask(generics.DestroyAPIView):
    serializer_class = TaskSerialiser

    def get_object(self):
        uuid = self.request.query_params.get('uuid')
        if uuid is not None:
            task = get_object_or_404(Task.objects.all(), uuid=uuid)
            return task
        else:
            return super().get_object()
