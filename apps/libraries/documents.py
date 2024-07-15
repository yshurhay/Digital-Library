from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Library


@registry.register_document
class LibraryDocument(Document):
    class Index:
        name = "libraries"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Library
        fields = [
            "name",
            "address"
        ]
