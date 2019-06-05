from django.db import models
from django import forms
from django.utils import timezone


class Participant(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=200)
  github = models.CharField(max_length=2000)
  github_nickname = models.CharField(max_length=200)
  codeforces = models.CharField(max_length=2000)
  codeforces_nickname = models.CharField(max_length=200)
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

class Testimonial(models.Model):
  author = models.CharField(max_length=50)
  program = models.CharField(max_length=50)
  content = models.CharField(max_length=100)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.author

class New(models.Model):
  title = models.CharField(max_length=50)
  subtitle = models.CharField(max_length=50)
  link = models.CharField(max_length=5000)
  published_date = models.DateTimeField(blank=True, null=True)
  

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

class Famous(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=200)
  github = models.CharField(max_length=2000)
  github_nickname = models.CharField(max_length=200)
  codeforces = models.CharField(max_length=2000)
  codeforces_nickname = models.CharField(max_length=200)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  class Meta:
    verbose_name_plural = 'Famous'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.name

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

class Event(models.Model):
  semester = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  content = models.CharField(max_length=50)
  published_date = models.DateTimeField(blank=True, null=True)


  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

