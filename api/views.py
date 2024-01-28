from django.shortcuts import render
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import generics
from bookstoreapp.models import *


# Create your views here.

class AuthorsList(generics.ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer

class BooksList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
