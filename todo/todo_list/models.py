from django.db import models
from django.contrib.auth import get_user_model

from .constants import ID_LENGTH
# from .core import UUID


User = get_user_model()


class Task(models.Model):
    uuid = models.CharField(
        verbose_name='Task unique id', editable=False,
        unique=True, max_length=ID_LENGTH
        )
    # uuid = UUID(
    #     verbose_name='Task unique id', editable=False,
    # )
    body = models.TextField(
        max_length=2000, blank=False, verbose_name='Task_description',
        help_text='Please enter task description here.',
        )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Date of creation'
        )
    active = models.BooleanField(default=True)
