from django.urls import path

from .views import BookListAPIView, AuthorListAPIView, GenreListAPIView


urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),
    path('genres/', GenreListAPIView.as_view()),
]
