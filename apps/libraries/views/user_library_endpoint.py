from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..serializers import UserLibrarySerializer
from ..models import UserLibrary


class UserLibraryListCreateAPIView(ListCreateAPIView):
    queryset = UserLibrary.objects.all()
    serializer_class = UserLibrarySerializer


class UserLibraryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserLibrary.objects.all()
    serializer_class = UserLibrarySerializer

