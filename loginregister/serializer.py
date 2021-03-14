from rest_framework import serializers
from .models import *
from rest_framework.response import Response


class Quiz_serializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
    