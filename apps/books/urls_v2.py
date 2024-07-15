from django.urls import path, re_path

from .views import (BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView,
                    AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView,
                    GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView,
                    SearchBooks)


urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    re_path('books/(?P<pk>[^/.]+)/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    re_path('book/search/(?P<query>[^/.]+)/', SearchBooks.as_view()),
    path('authors/', AuthorListCreateAPIView.as_view()),
    re_path('authors/(?P<pk>[^/.]+)/', AuthorRetrieveUpdateDestroyAPIView.as_view()),
    path('genres/', GenreListCreateAPIView.as_view()),
    re_path('genres/(?P<pk>[^/.]+)/', GenreRetrieveUpdateDestroyAPIView.as_view())
]
