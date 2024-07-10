from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..serializers import LibrarySerializer
from ..models import Library


class LibraryListCreateAPIView(ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class LibraryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
