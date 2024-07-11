from faker import Faker
from apps.libraries.models import Library

fake = Faker()


def create_libraries(num=10):
    for _ in range(num):
        Library.objects.create(
            name=fake.unique.company(),
            address=fake.unique.address(),
        )


def perform(*args, **kwargs):
    create_libraries()
