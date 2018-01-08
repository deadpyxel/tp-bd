from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from .forms import CursoForm
from .models import Curso, IntituicaoEnsinoSuperior


# TODO refactor code for class based views (50%)
# TODO Add Mantenedora views
# TODO Add Map views


# views Cursos
class CursosListView(generic.ListView):
    template_name = 'main/cursos.html'
    context_object_name = 'cursos'
    model = Curso
    paginate_by = 10

    def get_queryset(self):
        try:
            q = self.request.GET.get('q')
            if q is None:
                q = ''
        except:
            q = ''
        if q != '':
            object_list = self.model.objects.filter(nome_curso__icontains=q)
        else:
            object_list = self.model.objects.all()
        return object_list


class CursosDetailView(generic.DetailView):
    model = Curso
    template_name = 'main/curso_detail.html'


class CursoDeleteView(generic.DeleteView):
    model = Curso
    success_url = reverse_lazy('curso_list')


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
    return render(request, 'main/curso_update_form.html', {'form': form})


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
    return render(request, 'main/curso_update_form.html', {'form': form})


# views IES

class IESListView(generic.ListView):
    model = IntituicaoEnsinoSuperior
    template_name = 'main/ies.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            q = self.request.GET.get('q')
            if q is None:
                q = ''
        except:
            q = ''
        if q != '':
            object_list = self.model.objects.filter(nome_IES__icontains=q)
        else:
            object_list = self.model.objects.all()
        return object_list


class IESCreate(generic.CreateView):
    model = IntituicaoEnsinoSuperior
    fields = ['nome_IES', 'sigla_IES', 'email_IES']


class IESDetailView(generic.DetailView):
    model = IntituicaoEnsinoSuperior
    template_name = 'main/ies_detail.html'
    context_object_name = 'ies'


class IESUpdateView(generic.UpdateView):
    model = IntituicaoEnsinoSuperior
    fields = ['nome_IES', 'sigla_IES', 'email_IES']
    template_name = 'main/ies_update_form.html'


class IESDeleteView(generic.DeleteView):
    model = IntituicaoEnsinoSuperior
    success_url = reverse_lazy('ies_list')


# map

def map_view(request):
    return render(request, 'main/map.html')
