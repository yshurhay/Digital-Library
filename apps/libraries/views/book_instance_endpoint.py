from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..serializers import BookInstanceSerializer
from ..models import BookInstance


class BookInstanceListCreateAPIView(ListCreateAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer


class BookInstanceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer