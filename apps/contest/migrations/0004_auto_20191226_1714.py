# Generated by Django 2.2.8 on 2019-12-26 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_auto_20191226_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='end_date',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='contest',
            old_name='start_date',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='milestone',
            old_name='end_date',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='milestone',
            old_name='start_date',
            new_name='start_time',
        ),
    ]