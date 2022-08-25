from django.shortcuts import render

from familia.models import Familiares

# Create your views here.

def home(request):
    return render(request, 'home.html', context= {})

def ver_familia(request):
    persona = Familiares.objects.create(name="Maria", age=63, year='1959-08-20')
    persona1 = Familiares.objects.create(name="Pablo", age=65, year='1957-03-28')
    persona2 = Familiares.objects.create(name="Flor", age=26, year='1996-05-09')
    context = {'persona': persona, 'persona1': persona1, 'persona2': persona2 }
    return render (request, 'home.html', context)


