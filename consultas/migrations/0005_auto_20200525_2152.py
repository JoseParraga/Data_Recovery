# Generated by Django 3.0.5 on 2020-05-26 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0004_auto_20200523_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapperpublicaciones',
            old_name='cantidad_comentarios',
            new_name='cantidad_publicaciones',
        ),
    ]
