import string
import random

from todo_list.models import Task
from todo_list.constants import ID_LENGTH


class UuidGenerator1():
    def generate(self) -> str:
        id = ''.join(
            random.choices(string.digits + string.ascii_lowercase, k=ID_LENGTH)
        )
        if self.check(id):
            return self.generate()
        else:
            return id

    def check(self, id: str) -> bool:
        return Task.objects.filter(uuid=id).exists()


class UuidGenerator2():
    def generate(self) -> str:
        id = ''.join(
            random.choices(string.digits + string.ascii_lowercase, k=ID_LENGTH)
        )
        if Task.objects.filter(uuid=id).exists():
            return self.generate()
        else:
            return id


class UuidGenerator():
    def generate(self) -> str:
        id = None
        while self.check(id) or id is None:
            id = ''.join(
                random.choices(string.digits + string.ascii_lowercase,
                               k=ID_LENGTH)
            )
        return id

    def check(self, id: str) -> bool:
        return Task.objects.filter(uuid=id).exists()
