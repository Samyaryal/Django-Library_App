from rest_framework import generics 
from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):  #ListAPIView to create a read-only endpoint for all book instances.
  queryset = Book.objects.all() 
  serializer_class = BookSerializer
