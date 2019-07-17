from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response

from ..serializers import UserSerializer


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
