from rest_framework import serializers
from core.clients.models import *
from django.db.models.fields import CharField
from django.contrib.auth.hashers import make_password

class ClientSerializer(serializers.ModelSerializer):
    boss_name = serializers.CharField(source="boss.username", read_only=True)
    boss_email = serializers.CharField(source="boss.email", read_only=True)
    class Meta:
        model = Client
        fields = "__all__"
