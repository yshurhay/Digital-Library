from elasticsearch_dsl import Q
from rest_framework import status
from rest_framework.response import Response
from apps.libraries.documents import LibraryDocument
from apps.libraries.serializers import LibrarySerializer
from rest_framework.views import APIView


class SearchBooks(APIView):
    serializer_class = LibrarySerializer
    document_class = LibraryDocument

    @staticmethod
    def generate_q_expression(query):
        return Q(
            "multi_match", query=query, fields=[
                "name",
                "address"
            ], fuzziness='auto'
        )

    def get(self, request, query):
        if not query:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            return Response(self.serializer_class(search.to_queryset(), many=True).data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
