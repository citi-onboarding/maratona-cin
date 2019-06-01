from django.contrib import admin
from .models import Participant
from .models import Schedule
from .models import Medal

admin.site.register(Participant)
admin.site.register(Schedule)
admin.site.register(Medal)