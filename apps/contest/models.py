from django.db import models
from django.contrib.auth.models import User

from apps.participation.models import Team
from apps.resources.models import Document
from ..question.models import QuestionTypes, Question


# Create your models here.


class Contest(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=100)


class Milestone(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    contest = models.ForeignKey(Contest, related_name='milestones', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    team_size = models.PositiveSmallIntegerField()


class Task(models.Model):
    """ trial_cooldown: Should be in hours
    """
    milestone = models.ForeignKey(Milestone, related_name='tasks', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, unique=True)
    content = models.ForeignKey(Document, related_name='tasks', on_delete=models.CASCADE)
    trial_cooldown = models.PositiveSmallIntegerField()


class TeamTask(models.Model):
    task = models.ForeignKey(Task, related_name='team_tasks', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='tasks', on_delete=models.CASCADE)
    content_finished = models.BooleanField(default=False)
    max_trials_count = models.PositiveSmallIntegerField(default=3)
    last_trial_time = models.DateTimeField(null=True, blank=True)


class Trial(models.Model):
    team_task = models.ForeignKey(TeamTask, related_name='trials', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    due_time = models.DateTimeField()
    start_time = models.DateTimeField(auto_now_add=True)
    submit_time = models.DateTimeField(null=True, blank=True)


class TrialRecipe(models.Model):
    task = models.OneToOneField(Task, related_name='trial_recipe', on_delete=models.CASCADE)


class QuestionRecipe(models.Model):
    trial_recipe = models.ForeignKey(TrialRecipe, related_name='question_recipes', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=20, choices=QuestionTypes.TYPES)
    priority = models.PositiveSmallIntegerField()
    count = models.PositiveSmallIntegerField()


class QuestionSubmission(models.Model):
    trial = models.ForeignKey(Trial, related_name='question_submissions', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question_submissions', on_delete=models.CASCADE)
    answer = models.TextField()
    score = models.FloatField(default=0)