# Generated by Django 2.2.7 on 2019-12-06 07:51

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(choices=[('HS', 'دبیرستان'),
                                            (' BR', 'کارشناسی'), ('MR', 'کارشناسی ارشد'), ('PHD', 'دکنری')], default='HS', max_length=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name_en',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name_fa',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name_en',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name_fa',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='residence',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
