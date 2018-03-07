from django.contrib import admin

from .models import (
    Events,
    Details,
    RegistrationsAndParticipations,
    Hits,
    Media,
)
# Register your models here.

admin.site.register(Events)
admin.site.register(Details)
admin.site.register(RegistrationsAndParticipations)
admin.site.register(Hits)
admin.site.register(Media)

