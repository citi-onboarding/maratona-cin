from django.contrib import admin
from .models import Participant
from .models import Schedule

admin.site.register(Participant)
admin.site.register(Schedule)