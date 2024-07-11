from faker import Faker
from random import randint
from apps.libraries.models import UserLibrary
from apps.books.models import Book
from apps.users.models import User

fake = Faker()


def create_user_libraries(num=10):
    users = list(User.objects.all())
    books = list(Book.objects.all())

    for _ in range(num):
        user = fake.random_element(elements=users)
        user_library, created = UserLibrary.objects.get_or_create(user=user)

        random_books = fake.random_elements(elements=books, length=randint(1, len(books)))
        user_library.books.set(random_books)


def perform(*args, **kwargs):
    create_user_libraries()
