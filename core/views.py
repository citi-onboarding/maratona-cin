from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Participant
import math

def index(request):
    return render(request, 'index.html', {
      'participants':Participant.objects.all(),
      'containers_num':math.ceil(len(Participant.objects.all())/4)
      })