from django.shortcuts import render
from .models import Curso

def index(request):
    cursos = Curso.objects.all()
    return render(request, 'main/index.html', {'cursos': cursos})
