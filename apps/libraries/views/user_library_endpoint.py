from rest_framework.generics import ListAPIView

from ..serializers import UserLibrarySerializer
from ..models import UserLibrary


class UserLibraryListAPIView(ListAPIView):
    queryset = UserLibrary.objects.all()
    serializer_class = UserLibrarySerializer
