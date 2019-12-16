# Generated by Django 2.2.7 on 2019-12-06 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name_fa', models.TextField(max_length=100)),
                ('first_name_en', models.TextField(max_length=100)),
                ('last_name_fa', models.TextField(max_length=100)),
                ('last_name_en', models.TextField(max_length=100)),
                ('birth_date', models.DateTimeField()),
                ('residence', models.CharField(max_length=100)),
                ('education', models.CharField(choices=[('high_school', 'دبیرستان'), ('bachelor', 'کارشناسی'), ('master', 'کارشناسی ارشد'), ('phd', 'دکنری')], max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]