from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Participant
from .models import Schedule
from .models import Testimonial
import math



def index(request):
  # Organize participants by id
  i = 0
  object_list = list(Participant.objects.all().order_by('id'))
  object_sublist = list()
  slide = []
  for obj in object_list:
    if (i < 3):
      slide.append(obj)
      i += 1
    else:
      slide.append(obj)
      object_sublist.append(slide)
      slide = []
      i = 0
  object_sublist.append(slide)

  return render(request, 'index.html', {
    'Schedule': Schedule.objects.all().order_by('activity_date'),
    'participants':Participant.objects.all(),
    'object_list':object_sublist,
    'containers_num':math.ceil(len(Participant.objects.all())/4),
    'testimonials': Testimonial.objects.all(),
    })
