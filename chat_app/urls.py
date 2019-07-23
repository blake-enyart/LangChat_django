from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',  views.index, name='about'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    path('api/v1/users/', views.UserList.as_view(), name='registration'),
    path('api/v1/rooms/<int:room_id>/messages/', views.MessageList.as_view(), name='messages'),
]
