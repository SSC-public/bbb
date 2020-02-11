# Generated by Django 2.2.9 on 2020-02-11 00:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200209_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09001234567'. Up to 15 digits allowed.", regex='^0\\d{10}$')]),
        ),
    ]
