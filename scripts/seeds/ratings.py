from faker import Faker
from apps.comments.models import Rating
from apps.users.models import User
from apps.books.models import Book


fake = Faker()


def create_ratings(num=10):
    users = list(User.objects.all())
    books = list(Book.objects.all())

    for _ in range(num):
        Rating.objects.create(
            user=fake.random_element(elements=users),
            book=fake.random_element(elements=books),
            rating=fake.random_int(min=1, max=10)
        )


def perform(*args, **kwargs):
    create_ratings()
