import string
import random
# import datetime as dt

from todo_list.models import Task
from todo_list.constants import ID_LENGTH
# import django_filters
# from django_filters import filters


# class UuidGenerator1():
#     def generate(self) -> str:
#         id = ''.join(
#             random.choices(string.digits + string.ascii_lowercase,
# k=ID_LENGTH)
#         )
#         if self.check(id):
#             return self.generate()
#         else:
#             return id

#     def check(self, id: str) -> bool:
#         return Task.objects.filter(uuid=id).exists()


# class UuidGenerator2():
#     def generate(self) -> str:
#         id = ''.join(
#             random.choices(string.digits + string.ascii_lowercase,
# k=ID_LENGTH)
#         )
#         if Task.objects.filter(uuid=id).exists():
#             return self.generate()
#         else:
#             return id


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


# class DateFilter(django_filters.FilterSet):
#     created = filters.DateFromToRangeFilter(
#         field_name='created',
#         method='get_from_period',
#         label="from period",
#     )

#     def get_from_period(self, queryset, field_name, value):
#         start_str = self.request.query_params.get('start')
#         end_str = self.request.query_params.get('end')
#         if all(start_str is not None,
#                end_str is not None):
#             start_date = dt.datetime.strptime(start_str, '%d.%m.%y')
#             end_date = dt.datetime.strptime(end_str, '%d.%m.%y')
#             + dt.timedelta(days=1)
#             return queryset.filter(created__range=(start_date, end_date))
#         else:
#             return queryset

#     class Meta:
#         model = Task
#         fields = ('created',)
