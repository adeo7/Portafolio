from django.shortcuts import render
from .models import proyectos

def home(request):
    Lproyect=proyectos.objects.all()
    return render(request, 'home.html', {'proyectos': Lproyect})
