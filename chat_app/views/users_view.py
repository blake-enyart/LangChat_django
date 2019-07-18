from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import UserSerializer

# Mapping from post request keys to user columns in the db
conversion = {
    "displayName": "username",
    "firstName": "first_name",
    "lastName": "last_name",
    "active": "is_active",
    "countryOfOrigin": "country_of_origin",
    "password": "password",
    "passwordConfirmation": "password_confirmation"
}

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def post(self, request, format=None):
        parsed_data = {
            conversion[key]: value for key, value in request.data.items()
        }
        serializer = UserSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
