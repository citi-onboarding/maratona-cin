from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Participant

def index(request):
    return render(request, 'index.html', {'participants':Participant.objects.all()})