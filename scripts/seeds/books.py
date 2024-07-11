from faker import Faker
from apps.books.models import Book, Author, Genre


fake = Faker()


def create_books(num=10):
    authors = list(Author.objects.all())
    genres = list(Genre.objects.all())

    if not authors or not genres:
        return "Cannot create books because there are no authors or genres in the database"

    for _ in range(num):
        title = fake.sentence(nb_words=3)
        author = fake.random_element(elements=authors)
        genre = fake.random_element(elements=genres)
        year = fake.year()
        country = fake.country()
        description = fake.paragraph(nb_sentences=3)
        is_public = fake.boolean()

        Book.objects.create(
            title=title,
            author=author,
            genre=genre,
            year=year,
            country=country,
            description=description,
            is_public=is_public
        )


def perform(*args, **kwargs):
    create_books()
