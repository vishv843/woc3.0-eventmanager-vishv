from django.contrib import admin
from .models import *


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name', 'host_id')
class PartAdmin(admin.ModelAdmin):
    list_display = ('part_name', 'contact')

admin.site.register(register, RegisterAdmin)
admin.site.register(participant, PartAdmin)
