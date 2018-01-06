from django.shortcuts import render, get_object_or_404, redirect
from .forms import CursoForm
from .models import Curso


def index(request):
    cursos = Curso.objects.all()
    return render(request, 'main/index.html', {'cursos': cursos})


def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'main/curso_detail.html', {'curso': curso})


def curso_new(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            # curso.cod_IES = request.IES
            curso.save()
            return redirect('curso_detail', pk=curso.pk)
    else:
        form = CursoForm()
    return render(request, 'main/curso_edit.html', {'form': form})


def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            return redirect('curso_detail', pk=curso.pk)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'main/curso_edit.html', {'form': form})
