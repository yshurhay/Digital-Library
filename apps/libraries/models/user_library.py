from django.db import models

from apps.users.models import User
from apps.books.models import Book


class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.user.username
