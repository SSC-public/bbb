from django.db import models
from django.contrib.auth.models import User

from ..question.models import QuestionTypes


# Create your models here.

class ScoreStatusTypes:
    SCORED = 'scored'
    QUEUED = 'queued'
    JUDGING = 'judging'
    FAILED = 'failed'
    ERROR = 'error'
    TYPES = (
        (SCORED, 'scored'),
        (QUEUED, 'queued'),
        (JUDGING, 'judging'),
        (FAILED, 'failed'),
        (ERROR, 'error'),
    )


class Contest(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    team_size = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100, unique=True)


class Milestone(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    contest = models.ForeignKey('contest.Contest', related_name='milestones', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Task(models.Model):
    """
    trial_cooldown: Should be in hours
    """

    milestone = models.ForeignKey('contest.Milestone', related_name='tasks', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, unique=True)
    content = models.ForeignKey('resources.Document', related_name='tasks', on_delete=models.CASCADE)
    max_trials_count = models.PositiveSmallIntegerField(default=3)
    trial_cooldown = models.PositiveSmallIntegerField()
    trial_time = models.PositiveSmallIntegerField()


class TeamTask(models.Model):
    task = models.ForeignKey('contest.Task', related_name='team_tasks', on_delete=models.CASCADE)
    team = models.ForeignKey('participation.Team', related_name='tasks', on_delete=models.CASCADE)
    content_finished = models.BooleanField(default=False)
    final_score = models.FloatField(blank=True, null=True)


class Trial(models.Model):
    team_task = models.ForeignKey('contest.TeamTask', related_name='trials', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    due_time = models.DateTimeField()
    start_time = models.DateTimeField(auto_now_add=True)
    submit_time = models.DateTimeField(null=True, blank=True)


class TrialRecipe(models.Model):
    task = models.OneToOneField('contest.Task', related_name='trial_recipe', on_delete=models.CASCADE)


class QuestionRecipe(models.Model):
    trial_recipe = models.ForeignKey('contest.TrialRecipe', related_name='question_recipes', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=20, choices=QuestionTypes.TYPES)
    priority = models.PositiveSmallIntegerField()
    count = models.PositiveSmallIntegerField()


class QuestionSubmission(models.Model):
    trial = models.ForeignKey('contest.Trial', related_name='question_submissions', on_delete=models.CASCADE)
    question = models.ForeignKey('question.Question', related_name='question_submissions', on_delete=models.CASCADE)
    question_priority = models.PositiveSmallIntegerField()
    answer = models.TextField(blank=True, null=False)
    score = models.OneToOneField('contest.Score', related_name='question_submission', on_delete=models.CASCADE)


class Score(models.Model):
    number_score = models.FloatField(default=0)
    status = models.CharField(choices=ScoreStatusTypes.TYPES, max_length=10)
    info = models.CharField(max_length=1000, blank=True, null=False)
