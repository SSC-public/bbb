# Generated by Django 2.2.8 on 2019-12-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]