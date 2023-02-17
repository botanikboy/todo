import string
import random

from django.db import models

from .constants import ID_LENGTH


class UUID(models.CharField):
    def __init__(self, *args, **kwargs):
        options = {
            'max_length': ID_LENGTH,
            'unique': True,
        }
        options.update(kwargs)
        super().__init__(*args, **options)

    def get_default(self):
        generated_id = ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=ID_LENGTH)
            )
        return str(generated_id)
