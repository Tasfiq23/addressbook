from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
from core.models import Person
from .forms import PersonForm


def list_persons(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'all.html', context)


def new_person(request):
    form = PersonForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Contact added successfully.")
        return redirect('core:index')

    context = {
        'form': form
    }

    return render(request, 'new.html', context)


def delete_person(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('core:index')
