from faker import Faker
from apps.books.models import Author

fake = Faker()


def create_authors(num=10):
    for _ in range(num):
        Author.objects.create(
            first_name=fake.unique.first_name(),
            last_name=fake.unique.last_name()
        )


def perform(*args, **kwargs):
    create_authors()
