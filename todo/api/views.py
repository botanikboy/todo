from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

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
