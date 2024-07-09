from rest_framework.generics import ListAPIView

from ..serializers import RatingSerializer
from ..models import Rating


class RatingListAPIView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
