# Generated by Django 3.2 on 2021-09-24 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='tag',
            new_name='tags',
        ),
    ]