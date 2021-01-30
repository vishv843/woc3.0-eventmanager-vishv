from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_ID', 'event_name', 'email_ID')
class PartAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')

admin.site.register(event, EventAdmin)
admin.site.register(participant, PartAdmin)
