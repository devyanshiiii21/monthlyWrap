# Generated by Django 4.2.1 on 2024-03-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_categories_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='tech_used',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.AddField(
            model_name='projects',
            name='tech_used',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
