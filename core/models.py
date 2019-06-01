from django.db import models
from django.utils import timezone


class Participant(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  github = models.CharField(max_length=200)
  github_nickname = models.CharField(max_length=200)
  codeforces = models.CharField(max_length=200)
  codeforces_nickname = models.CharField(max_length=200)
  id = models.IntegerField(primary_key=True)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.name

class Schedule(models.Model):
  activity = models.CharField(max_length=150)
  activity_date = models.DateTimeField(blank = False, default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.activity

class Medal(models.Model):

  Primeiro = 'Primeiro Lugar'
  Segundo = 'Segundo Segundo'
  Terceiro = 'Terceiro Lugar'

  POSITION_CHOICES = [(Primeiro, 'Primeiro Lugar'),(Segundo, 'Segundo Lugar'),(Terceiro, 'Terceiro Lugar')]

  Nacional = 'Nacional'
  Internacional = 'Internacional'

  TYPE_CHOICES = [(Nacional, 'Nacional'),(Internacional, 'Internacional')]

  type = models.CharField(max_length=50, choices = TYPE_CHOICES) 
  position = models.CharField(max_length=50, choices=POSITION_CHOICES)
  title_name = models.CharField(max_length=150)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title_name
