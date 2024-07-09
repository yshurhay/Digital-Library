from rest_framework.generics import ListAPIView

from ..serializers import CommentSerializer
from ..models import Comment


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
