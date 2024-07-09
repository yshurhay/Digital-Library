from rest_framework.generics import ListAPIView

from ..serializers import GenreSerializer
from ..models import Genre


class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
