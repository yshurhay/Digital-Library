from rest_framework.serializers import ModelSerializer
from ..models import BookInstance


class BookInstanceSerializer(ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ['book', 'library', 'is_available', 'due_back']
