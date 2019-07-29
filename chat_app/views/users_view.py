from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserSerializer

from drf_yasg.utils import swagger_auto_schema

# Mapping from post request keys to user columns in the db
conversion = {
    "displayName": "username",
    "firstName": "first_name",
    "lastName": "last_name",
    "active": "is_active",
    "countryOfOrigin": "country_of_origin",
    "password": "password",
    "passwordConfirmation": "password_confirmation",
    "email": "email"
}

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        operation_description="Create a new user",
        security=[],
        tags=['Users'],
        query_serializer=UserSerializer,
    )
    def post(self, request, format=None):
        parsed_data = {
            conversion[key]: value for key, value in request.data.items()
        }
        serializer = UserSerializer(data=parsed_data)
        if serializer.is_valid():
            if serializer.save():
                user = get_user_model().objects.last()
                token, created = Token.objects.get_or_create(user=user)
                user_data = serializer.data
                user_data['token'] = token.key
                return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
