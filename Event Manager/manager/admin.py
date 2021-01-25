from django.contrib import admin
from .models import *


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name', 'host_id')

admin.site.register(register, RegisterAdmin)
