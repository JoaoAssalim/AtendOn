from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()
            if user is None:
                raise serializers.ValidationError('Invalid login credentials.')
            attrs['user'] = user
        else:
            raise serializers.ValidationError('Both username and password are required.')

        return attrs