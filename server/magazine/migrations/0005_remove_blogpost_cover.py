# Generated by Django 4.2.1 on 2023-06-03 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_rename_author_comment_user_blogpost_likes_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='cover',
        ),
    ]
