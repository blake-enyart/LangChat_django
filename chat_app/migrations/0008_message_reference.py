# Generated by Django 2.2.3 on 2019-07-22 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0007_auto_20190722_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referenced_message', to='chat_app.Message'),
        ),
    ]
