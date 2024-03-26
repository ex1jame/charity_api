from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from . import serializers

User = get_user_model()
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
    permission_classes = [permissions.IsAuthenticated,]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated,]