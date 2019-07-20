from django.contrib.auth import get_user_model, login, logout # new
from django.contrib.auth.forms import AuthenticationForm # new
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status, views # new
from rest_framework.response import Response

from ..serializers import UserSerializer

class LogInView(views.APIView):
    """
    POST api/v1/log_in/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user=form.get_user())
            user_hash = UserSerializer(user).data
            token, created = Token.objects.get_or_create(user=user)
            user_hash['token'] = token.key
            return Response(user_hash)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, *args, **kwargs):
        logout(self.request)
        return Response(status=status.HTTP_204_NO_CONTENT)
