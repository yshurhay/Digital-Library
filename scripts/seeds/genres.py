from faker import Faker
from apps.books.models import Genre

fake = Faker()


def create_genres(num=10):
    for _ in range(num):
        name = fake.unique.word().capitalize()
        if not Genre.objects.filter(name=name).exists():
            Genre.objects.create(name=name)


def perform(*args, **kwargs):
    create_genres()

