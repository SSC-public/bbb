# Generated by Django 2.2.9 on 2020-02-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20200224_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='description',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='link',
            field=models.URLField(max_length=400, null=True),
        ),
    ]
