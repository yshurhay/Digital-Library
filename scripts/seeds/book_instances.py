from faker import Faker
from apps.libraries.models import Library, BookInstance
from apps.books.models import Book


fake = Faker()


def create_instances(num=10):
    library = list(Library.objects.all())
    books = list(Book.objects.all())

    for _ in range(num):
        BookInstance.objects.create(
            book=fake.random_element(elements=books),
            library=fake.random_element(elements=library),
            is_available=fake.boolean(),
            due_back=fake.future_date()
        )


def perform(*args, **kwargs):
    create_instances()
