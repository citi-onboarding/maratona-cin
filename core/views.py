from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Participant
from .models import Schedule
from .models import Testimonial
from .models import New
from .models import Medal


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

  # Organize news by groups of 3
  j = 0
  new_list = list(New.objects.all())
  new_sublist = list()
  slide = []
  for new in new_list:
    if (j < 2):
      slide.append(new)
      j += 1
    else:
      slide.append(new)
      new_sublist.append(slide)
      slide = []
      j = 0
  new_sublist.append(slide)

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
    'object_list':object_sublist,
    'new_list':new_sublist,
    'containers_num':math.ceil(len(Participant.objects.all())/4),
    'testimonials': Testimonial.objects.all(),
    })
