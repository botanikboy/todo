from http import HTTPStatus

from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from todo_list.models import Task
from .serializers import TaskSerialiser
from .core import UuidGenerator


class CreateTask(GenericViewSet, generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser

    def perform_create(self, serializer):
        if serializer.is_valid():
            code = UuidGenerator()
            uuid = code.generate()
            serializer.save(uuid=uuid)


class ListTask(GenericViewSet, generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialiser


class RetriveDeleteTask(ViewSet):
    queryset = Task.objects.all()

    def retrieve(self, request, pk=None):
        uuid = request.query_params.get('uuid')
        task = get_object_or_404(self.queryset, uuid=uuid)
        serializer = TaskSerialiser(task)
        return Response(serializer.data)

    def destroy(self, request):
        uuid = request.query_params.get('uuid')
        task = get_object_or_404(self.queryset, uuid=uuid)
        try:
            self.perform_destroy(task)
        except Exception:
            pass
        return Response(status=HTTPStatus.NO_CONTENT)
