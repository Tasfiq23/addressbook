from django.contrib import admin
from .models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'street_address', 'state', 'postcode']

admin.site.register(Person, PersonAdmin)
