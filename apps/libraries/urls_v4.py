from django.urls import path

from .views import LibraryListAPIView, BookInstanceListAPIView, UserLibraryListAPIView


urlpatterns = [
    path('libraries/', LibraryListAPIView.as_view()),
    path('instances/', BookInstanceListAPIView.as_view()),
    path('user-libraries/', UserLibraryListAPIView.as_view()),
]
