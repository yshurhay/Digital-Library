from django.urls import path, re_path

from .views import (LibraryListCreateAPIView, LibraryRetrieveUpdateDestroyAPIView,
                    BookInstanceListCreateAPIView, BookInstanceRetrieveUpdateDestroyAPIView,
                    UserLibraryListCreateAPIView, UserLibraryRetrieveUpdateDestroyAPIView)


urlpatterns = [
    path('user-libraries/', UserLibraryListCreateAPIView.as_view()),
    re_path('user-libraries/(?P<pk>[^/.]+)', UserLibraryRetrieveUpdateDestroyAPIView.as_view()),
    path('libraries/', LibraryListCreateAPIView.as_view()),
    re_path('libraries/(?P<pk>[^/.]+)', LibraryRetrieveUpdateDestroyAPIView.as_view()),
    path('instances/', BookInstanceListCreateAPIView.as_view()),
    re_path('instances/(?P<pk>[^/.]+)', BookInstanceRetrieveUpdateDestroyAPIView.as_view()),
]
