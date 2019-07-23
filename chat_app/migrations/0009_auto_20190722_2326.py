# Generated by Django 2.2.3 on 2019-07-22 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0008_message_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referenced_message', to='chat_app.Message'),
        ),
    ]