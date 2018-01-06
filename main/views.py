from django.shortcuts import render, get_object_or_404
from .models import Curso


def index(request):
    cursos = Curso.objects.all()
    return render(request, 'main/index.html', {'cursos': cursos})


def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'main/curso_detail.html', {'curso': curso})
