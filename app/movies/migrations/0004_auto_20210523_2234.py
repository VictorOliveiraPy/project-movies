# Generated by Django 3.2.3 on 2021-05-23 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_yar_movie_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='updated_data',
            new_name='updated_date',
        ),
    ]