from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..serializers import BookSerializer
from ..models import Book


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
