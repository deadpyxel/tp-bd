from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import CursoForm
from .models import Curso, IntituicaoEnsinoSuperior


# views Cursos
class CursosListView(generic.ListView):
    template_name = 'main/cursos.html'

    def get_queryset(self):
        return Curso.objects.all()


class CursosDetailView(generic.DetailView):
    model = Curso
    template_name = 'main/curso_detail.html'


def index(request):
    return render(request, 'main/index.html')


def curso_new(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
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


# views IES

class IESListView(generic.ListView):
    template_name = 'main/ies.html'

    def get_queryset(self):
        return IntituicaoEnsinoSuperior.objects.all()


class IESDetailView(generic.DetailView):
    model = IntituicaoEnsinoSuperior
    template_name = 'main/ies_detail.html'
    context_object_name = 'ies'


class IESUpdateView(generic.UpdateView):
    model = IntituicaoEnsinoSuperior
    fields = ['nome_IES', 'sigla_IES', 'email_IES']
    template_name = 'main/ies_update_form.html'
