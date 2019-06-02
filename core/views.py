from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Participant
from .models import Schedule
from .models import Medal
import math



def index(request):

  k = 0
  nacional_list = list(Medal.objects.all())
  nacional_sublist = list()
  slide_nacional = []
  for medal in nacional_list:
    if medal.type == 'Nacional':
      if (k < 1):
        slide_nacional.append(medal)
        k += 1
      else:
        slide_nacional.append(medal)
        nacional_sublist.append(slide_nacional)
        slide_nacional = []
        k = 0
  nacional_sublist.append(slide_nacional)

  l = 0
  internacional_list = list(Medal.objects.all())
  internacional_sublist = list()
  slide_internacional = []
  for medal in internacional_list:
    if medal.type == 'Internacional':
      if (l < 2):
        slide_internacional.append(medal)
        l += 1
      else:
        slide_internacional.append(medal)
        internacional_sublist.append(slide_internacional)
        slide_internacional = []
        l = 0
  internacional_sublist.append(slide_internacional)

  return render(request, 'index.html', {
    'Medal': Medal.objects.all().order_by('type'),
    'nacional_list': nacional_sublist,
    'internacional_list': internacional_sublist,
    'Schedule': Schedule.objects.all().order_by('activity_date'),
    'participants':Participant.objects.all(),
    'containers_num':math.ceil(len(Participant.objects.all())/4)
    })
