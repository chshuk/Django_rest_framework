# Generated by Django 4.1.4 on 2023-01-18 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applic', '0010_rename_create_article_create_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='create_time',
        ),
    ]
