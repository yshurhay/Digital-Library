from .authors_endpoint import AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView
from .books_endpoint import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView
from .genres_endpoint import GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView

__all__ = (
    'AuthorListCreateAPIView',
    'AuthorRetrieveUpdateDestroyAPIView',
    'BookListCreateAPIView',
    'BookRetrieveUpdateDestroyAPIView',
    'GenreListCreateAPIView',
    'GenreRetrieveUpdateDestroyAPIView',
)
