# Generated by Django 4.1.4 on 2023-01-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applic', '0013_remove_article_create_remove_article_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='applic.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
