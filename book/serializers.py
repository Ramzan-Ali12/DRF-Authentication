from rest_framework import serializers
from .models import Book
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        book = Book.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
            author=validated_data['author'],
        )
        return book
