from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'street_address', 'state', 'postcode']
