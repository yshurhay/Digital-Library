from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'