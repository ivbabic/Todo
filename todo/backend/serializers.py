from rest_framework import serializers
from backend.models import  *
from django.contrib.auth import get_user_model

User = get_user_model()


class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('id', 'desc', 'date_add', 'date_todo', 'done', 'user')