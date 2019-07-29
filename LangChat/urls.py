"""LangChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from chat_app.views import LogInView, LogOutView

schema_view = get_schema_view(
   openapi.Info(
      title="LangChat API",
      default_version='v1',
      description="To demo, use the following user: \
      \n * username: blakeenyart \
      \n * password: password",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(name="Blake Enyart", email="blake.enyart@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   url=settings.CURRENT_HOST,
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/log_in/', LogInView.as_view(), name='log_in'),
    path('api/v1/log_out/', LogOutView.as_view(), name='log_out'),
    re_path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('chat_app.urls')),
]
