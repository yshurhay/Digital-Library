from django.db import models

from .library import Library
from apps.books.models import Book


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    due_back = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} ({self.library.name})"
