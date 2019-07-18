from django.contrib.auth import get_user_model, login, logout # new
from django.contrib.auth.forms import AuthenticationForm # new
from rest_framework import generics, permissions, status, views # new
from rest_framework.response import Response

from ..serializers import UserSerializer

class LogInView(views.APIView): # new
    def post(self, request):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user=form.get_user())
            return Response(UserSerializer(user).data)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(views.APIView): # new
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, *args, **kwargs):
        logout(self.request)
        return Response(status=status.HTTP_204_NO_CONTENT)
