from faker import Faker
from apps.comments.models import Comment
from apps.users.models import User
from apps.books.models import Book


fake = Faker()


def create_comments(num=10):
    users = list(User.objects.all())
    books = list(Book.objects.all())

    for _ in range(num):
        Comment.objects.create(
            user=fake.random_element(elements=users),
            book=fake.random_element(elements=books),
            text=fake.paragraph(nb_sentences=4),
            created_at=fake.date_time_this_year()
        )


def perform(*args, **kwargs):
    create_comments()
