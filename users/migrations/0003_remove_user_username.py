# Generated by Django 5.0.8 on 2024-09-20 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
