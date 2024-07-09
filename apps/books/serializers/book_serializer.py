from rest_framework.serializers import ModelSerializer

from ..models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year', 'country', 'description', 'is_public']
