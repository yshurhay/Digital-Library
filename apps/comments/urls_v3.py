from django.urls import path, re_path

from .views import (CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView,
                    RatingListCreateAPIView, RatingRetrieveUpdateDestroyAPIView)


urlpatterns = [
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    re_path('comments/(?P<pk>[^/.]+)', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    path('ratings/', RatingListCreateAPIView.as_view()),
    re_path('ratings/(?P<pk>[^/.]+)', RatingRetrieveUpdateDestroyAPIView.as_view()),
]
