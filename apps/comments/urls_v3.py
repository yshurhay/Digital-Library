from django.urls import path

from .views import CommentListAPIView, RatingListAPIView


urlpatterns = [
    path('comments/', CommentListAPIView.as_view()),
    path('ratings/', RatingListAPIView.as_view()),
]
