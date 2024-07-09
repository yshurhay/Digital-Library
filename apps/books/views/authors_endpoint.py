from rest_framework.generics import ListAPIView

from ..serializers import AuthorSerializer
from ..models import Author


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
