from django.db import models
from apps.users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.books.models import Book


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return f"Rating {self.rating} by {self.user.username} on {self.book.title}"
