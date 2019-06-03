from django.contrib import admin
from .models import Testimonial
from .models import New
from .models import Participant
from .models import Schedule
from .models import Medal
from .models import Famous

admin.site.register(Testimonial)
admin.site.register(New)
admin.site.register(Participant)
admin.site.register(Schedule)
admin.site.register(Medal)
admin.site.register(Famous)
