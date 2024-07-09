from rest_framework.generics import ListAPIView

from ..serializers import BookSerializer
from ..models import Book


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
