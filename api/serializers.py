from rest_framework import serializers
from bookstoreapp.models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'