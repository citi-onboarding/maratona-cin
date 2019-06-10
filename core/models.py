from django.db import models
from django import forms
from django.utils import timezone

class Participant(models.Model):

  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=200)
  github = models.CharField(max_length=2000)
  codeforces = models.CharField(max_length=2000)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.name

class Schedule(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  activity = models.CharField(max_length=150)
  activity_date = models.DateTimeField(blank = False, default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.activity

class Testimonial(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  student = models.CharField(max_length=50)
  program = models.CharField(max_length=50)
  content = models.CharField(max_length=100)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.student

class New(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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
  github = models.CharField(max_length=200)
  codeforces = models.CharField(max_length=200)
  description = models.TextField(max_length=400)
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
  Segundo = 'Segundo Lugar'
  Terceiro = 'Terceiro Lugar'

  POSITION_CHOICES = [(Primeiro, 'Primeiro Lugar'),(Segundo, 'Segundo Lugar'),(Terceiro, 'Terceiro Lugar')]

  Nacional = 'Nacional'
  Internacional = 'Internacional'

  TYPE_CHOICES = [(Nacional, 'Nacional'),(Internacional, 'Internacional')]

  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  type = models.CharField(max_length=50, choices = TYPE_CHOICES) 
  position = models.CharField(max_length=50, choices=POSITION_CHOICES)
  title_name = models.CharField(max_length=150)
  published_date = models.DateTimeField(blank=True, null=True)

  def getImage(self):
    if self.type == 'Nacional' and self.position == 'Primeiro Lugar':
      self.image = 'media/medal-national-gold.svg'
    elif self.type == 'Nacional' and self.position == 'Segundo Lugar':
      self.image = 'media/medal-national-silver.svg'
    elif self.type == 'Nacional' and self.position == 'Terceiro Lugar':
      self.image = 'media/medal-national-bronze.svg'
    elif self.type == 'Internacional' and self.position == 'Primeiro Lugar':
      self.image = 'media/medal-international-gold.svg'
    elif self.type == 'Internacional' and self.position == 'Segundo Lugar':
      self.image = 'media/medal-international-silver.svg'
    elif self.type == 'Internacional' and self.position == 'Terceiro Lugar':
      self.image = 'media/medal-international-bronze.svg'
    else:
      self.image = 'None'

    return self.image

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title_name

class Event(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  semester = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  content = models.CharField(max_length=50)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title