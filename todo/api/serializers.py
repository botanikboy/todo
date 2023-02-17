from rest_framework.serializers import ModelSerializer

from todo_list.models import Task


class TaskSerialiser(ModelSerializer):
    class Meta():
        model = Task
        fields = ('uuid', 'body', 'created', 'active')
        read_only_fields = ('uuid', 'created')
