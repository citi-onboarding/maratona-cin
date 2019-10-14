from django.db import models
from django import forms
from django.utils import timezone

class Information(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  facebook = models.CharField(max_length=50)
  instagram = models.CharField(max_length=50)
  email = models.CharField(max_length=50)

  class Meta:
    verbose_name = 'Informação'
    verbose_name_plural = 'Informações'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return 'Information'

class Participant(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  image = models.FileField(upload_to='time/')
  email = models.CharField(max_length=200)
  codeforces_user = models.CharField(max_length=2000)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  class Meta:
    verbose_name = 'Participante'
    verbose_name_plural = 'Participantes'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.name

class Schedule(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  activity = models.CharField(max_length=150)
  description = models.TextField(max_length=400)
  activity_date = models.DateTimeField(blank = False, default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  class Meta:
    verbose_name = 'Atividade'
    verbose_name_plural = 'Atividades'

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

  class Meta:
    verbose_name = 'Depoimento'
    verbose_name_plural = 'Depoimentos'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.student

class New(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  subtitle = models.CharField(max_length=50)
  icon = models.FileField(upload_to='noticias-icones/')
  link = models.CharField(max_length=100)
  published_date = models.DateTimeField(blank=True, null=True)

  class Meta:
    verbose_name = 'Notícia'
    verbose_name_plural = 'Notícias'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

class Famous(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  image = models.FileField(upload_to='hall-da-fama/')
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=200, blank=True, default='')
  codeforces = models.CharField(max_length=200, blank=True, default='')
  description = models.TextField(max_length=400)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  class Meta:
    verbose_name = 'Famoso'
    verbose_name_plural = 'Hall da Fama'

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

  class Meta:
    verbose_name = 'Medalha'
    verbose_name_plural = 'Medalhas'

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
  image = models.FileField(upload_to='eventos/')
  semester = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  content = models.CharField(max_length=50)
  published_date = models.DateTimeField(blank=True, null=True)

  class Meta:
    verbose_name = 'Evento'
    verbose_name_plural = 'Eventos'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title

class Partner(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  logo = models.FileField(upload_to='parceiros/')

  class Meta:
    verbose_name = 'Parceiro'
    verbose_name_plural = 'Parceiros'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.name

class Link(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  icon = models.FileField(upload_to='link-icons/')
  title = models.CharField(max_length= 50)
  link = models.CharField(max_length=100)

  class Meta:
    verbose_name = 'Link'
    verbose_name_plural = 'Links'

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.title
