from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',  views.about, name='about'),
    path('new/', views.new_room, name='new_room'),
    re_path(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]
