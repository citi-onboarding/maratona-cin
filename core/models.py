from django.db import models
from django import forms
from django.utils import timezone


class Participant(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=200)
  github = models.CharField(max_length=200)
  github_nickname = models.CharField(max_length=200)
  codeforces = models.CharField(max_length=200)
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
  