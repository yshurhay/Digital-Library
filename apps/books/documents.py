from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Book


@registry.register_document
class BookDocument(Document):
    genre = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField()
    })

    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField()
    })

    class Index:
        name = "books"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Book
        fields = [
            "title",
            "country",
            "description",
        ]
