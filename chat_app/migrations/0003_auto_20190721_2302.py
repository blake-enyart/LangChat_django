# Generated by Django 2.2.3 on 2019-07-21 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_user_country_of_origin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='handle',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
