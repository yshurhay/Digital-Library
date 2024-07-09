from rest_framework.serializers import ModelSerializer
from ..models import UserLibrary


class UserLibrarySerializer(ModelSerializer):
    class Meta:
        model = UserLibrary
        fields = ['user', 'books']
