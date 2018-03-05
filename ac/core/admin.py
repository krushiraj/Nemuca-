from django.contrib import admin

from .models import (
    Events,
    EventDetails,
    RegistrationsAndParticipations,
    Hits,
    Media,
)
# Register your models here.

admin.site.register(Events)
admin.site.register(EventDetails)
admin.site.register(RegistrationsAndParticipations)
admin.site.register(Hits)
admin.site.register(Media)

