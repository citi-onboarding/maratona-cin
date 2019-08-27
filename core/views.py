from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Participant
from .models import Schedule
from .models import Testimonial
from .models import New
from .models import Medal
from .models import Famous
from .models import Event
from .models import Link
from .models import Information
from .models import Partner


def index(request):
  # Organize participants by id
  i = 0
  object_list = list(Participant.objects.all().order_by('name'))
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
      if (l < 1):
        slide_internacional.append(medal)
        l += 1
      else:
        slide_internacional.append(medal)
        internacional_sublist.append(slide_internacional)
        slide_internacional = []
        l = 0
  internacional_sublist.append(slide_internacional)

  m = 0
  famous_list = list(Famous.objects.all().order_by('name'))
  famous_sublist = list()
  slide = []
  for famous in famous_list:
    if (m < 3):
      slide.append(famous)
      m += 1
    else:
      slide.append(famous)
      famous_sublist.append(slide)
      slide = []
      m = 0
  famous_sublist.append(slide)

  events = list(Event.objects.all().order_by('semester'))
  event_sublist = list()
  year_pack = {}
  for event in events:
    year = event.semester.split('.')[0]
    if (year in year_pack):
      year_pack[year].append(event)
    else:
      year_pack[year] = [event]

  # Organize news by groups of 3
  n = 0
  link_list = list(Link.objects.all())
  link_sublist = list()
  slide = []
  for link in link_list:
    if (n < 2):
      slide.append(link)
      n += 1
    else:
      slide.append(link)
      link_sublist.append(slide)
      slide = []
      n = 0



  return render(request, 'index.html', {
    'Medal': Medal.objects.all().order_by('type'),
    'nacional_list': nacional_sublist,
    'internacional_list': internacional_sublist,
    'Schedule': Schedule.objects.all().order_by('activity_date'),
    'famous_list': famous_sublist,
    'object_list':object_sublist,
    'new_list':new_sublist,
    'testimonials': Testimonial.objects.all(),
    'events': year_pack,
    'partners': Partner.objects.all(),
    'links': link_sublist,
    'info': Information.objects.all()[0],
    })
