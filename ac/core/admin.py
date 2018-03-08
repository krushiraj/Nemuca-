from django.contrib import admin

from .models import (
    Event,
    Details,
    RegistrationsAndParticipations,
    Hits,
    Media,
)
# Register your models here.

admin.site.register(Event)
admin.site.register(Details)
admin.site.register(RegistrationsAndParticipations)
admin.site.register(Hits)
admin.site.register(Media)
admin.site.register(Profile)

