# Generated by Django 2.2.3 on 2019-07-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0005_auto_20190721_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]