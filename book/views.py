from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from .models import Book
@api_view(["POST"])
def add(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            response_data = {
                'success': 'Book record added successfully',
                'book': {
                    'id': book.id,
                    'title': book.title,
                    'content': book.content,
                    'author': book.author,
                    'date_created': book.date_created,
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

