from rest_framework.generics import ListAPIView

from ..serializers import LibrarySerializer
from ..models import Library


class LibraryListAPIView(ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
