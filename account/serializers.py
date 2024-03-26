from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


User = get_user_model()



class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    company = serializers.CharField( required=True, max_length=150)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        min_length=8, write_only=True, required=True)
    password2 = serializers.CharField(
        min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        exclude = ('groups', 'username', 'user_permissions', 'is_superuser', 'is_staff', 'is_active')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        if password2 != attrs['password']:
            raise serializers.ValidationError('Passwords didn\'t match!')
        validate_password(attrs['password'])
        return attrs

    def validate_first_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError('Name must start with uppercase letter!')
        return value

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'company', 'first_name', 'last_name')

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password', 'is_staff','user_permissions')
