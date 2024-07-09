from rest_framework.generics import ListAPIView

from ..serializers import BookInstanceSerializer
from ..models import BookInstance


class BookInstanceListAPIView(ListAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
