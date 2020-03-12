from django.contrib import admin
from Manage_events.models import Category,Ticket,Event

# Register your models here.
admin.site.register(Ticket)


admin.site.register(Event)

admin.site.register(Category)
