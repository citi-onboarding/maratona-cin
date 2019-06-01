from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Participant
from .models import Schedule
from .models import Medal
import math



def index(request):
  return render(request, 'index.html', {
    'Medal': Medal.objects.all().order_by('type'),
    'Schedule': Schedule.objects.all().order_by('activity_date'),
    'participants':Participant.objects.all(),
    'containers_num':math.ceil(len(Participant.objects.all())/4)
    })
