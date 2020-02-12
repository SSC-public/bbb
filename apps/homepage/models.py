from django.db import models
from django.core.exceptions import ValidationError


class Intro(models.Model):
    header_en = models.CharField(max_length=100)
    header_fa = models.CharField(max_length=100)
    text_en = models.TextField()
    text_fa = models.TextField()

    term_of_use = models.TextField(null=True)

    def __str__(self):
        return self.header_en


class TimelineEvent(models.Model):
    date = models.DateTimeField()
    title_en = models.CharField(max_length=100)
    title_fa = models.CharField(max_length=100)
    text_en = models.TextField()
    text_fa = models.TextField()

    order = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title_en


class Prize(models.Model):
    title_en = models.CharField(max_length=100)
    title_fa = models.CharField(max_length=100)
    prize_en = models.CharField(max_length=100)
    prize_fa = models.CharField(max_length=100)

    def __str__(self):
        return self.title_en


class Stat(models.Model):
    title_en = models.CharField(max_length=100)
    title_fa = models.CharField(max_length=100)
    stat_en = models.CharField(max_length=100)
    stat_fa = models.CharField(max_length=100)

    def __str__(self):
        return self.title_en


class Count(models.Model):
    title = models.CharField(max_length=200)
    app_name = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    show = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        try:
            exec(f'from apps.{self.app_name} import models as m')
            eval(f'm.{self.model_name}.objects.count()')
        except Exception as e:
            raise ValidationError(str(e))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.app_name}.{self.model_name}'
