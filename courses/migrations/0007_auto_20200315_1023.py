# Generated by Django 3.0.4 on 2020-03-15 09:23

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('courses', '0006_auto_20200315_0959'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Klasa',
        ),
        migrations.RenameField(
            model_name='klasa',
            old_name='image',
            new_name='imazhi',
        ),
        migrations.RenameField(
            model_name='klasa',
            old_name='short_description',
            new_name='pershkrimi',
        ),
        migrations.RenameField(
            model_name='klasa',
            old_name='title',
            new_name='titulli',
        ),
    ]
