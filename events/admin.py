from django.contrib import admin
from .models import Event,EventPoster,Categories,Submission,Applauders,Volunteers,SeatWarmers,City

# Register your models here.
admin.site.register(Event)
admin.site.register(EventPoster)
admin.site.register(Categories)
admin.site.register(Submission)
admin.site.register(Applauders)
admin.site.register(Volunteers)
admin.site.register(SeatWarmers)
admin.site.register(City)