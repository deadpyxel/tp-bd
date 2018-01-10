from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.views import generic
from .models import Curso, IntituicaoEnsinoSuperior


# TODO refactor code for class based views (50%)
# TODO Add Mantenedora views
# TODO Add Map views


def index(request):
    return render(request, 'main/index.html')


# views Cursos
class CursoListView(generic.ListView):
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


class CursoCreateView(generic.CreateView):
    model = Curso
    fields = ['nome_curso', 'data_inicio_oferta', 'cod_IES', 'carga_horaria',
              'modalidade', 'nivel_curso', 'periodo', 'curso_gratuito',
              'num_vagas', 'possui_acessabilidade']
    template_name = 'main/curso_create_form.html'


class CursoUpdateView(generic.UpdateView):
    model = Curso
    fields = ['nome_curso', 'data_inicio_oferta', 'cod_IES', 'carga_horaria',
              'modalidade', 'nivel_curso', 'periodo', 'curso_gratuito',
              'num_vagas', 'possui_acessabilidade']
    template_name = 'main/curso_update_form.html'


class CursoDetailView(generic.DetailView):
    model = Curso
    template_name = 'main/curso_detail.html'


class CursoDeleteView(generic.DeleteView):
    model = Curso
    success_url = reverse_lazy('curso-list')


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


class IESCreateView(generic.CreateView):
    model = IntituicaoEnsinoSuperior
    fields = ['nome_IES', 'sigla_IES', 'email_IES', 'cod_mant',
              'organizacao_academica', 'rede', 'departamento_administrativo',
              'cep']
    template_name = 'main/ies_create_form.html'


class IESDetailView(generic.DetailView):
    model = IntituicaoEnsinoSuperior
    context_object_name = 'ies'
    template_name = 'main/ies_detail.html'


class IESUpdateView(generic.UpdateView):
    model = IntituicaoEnsinoSuperior
    fields = ['nome_IES', 'sigla_IES', 'email_IES', 'cod_mant',
              'organizacao_academica', 'rede', 'departamento_administrativo',
              'cep']
    template_name = 'main/ies_update_form.html'


class IESDeleteView(generic.DeleteView):
    model = IntituicaoEnsinoSuperior
    success_url = reverse_lazy('ies-list')
    template_name = 'main/ies_confirm_delete.html'


# map

def map_view(request):
    return render(request, 'main/map.html')
