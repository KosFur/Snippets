# Generated by Django 4.1.7 on 2024-08-29 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_snippet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
