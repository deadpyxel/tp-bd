from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = (
            'nome_curso', 'data_inicio_oferta', 'cod_IES', 'carga_horaria',
            'modalidade', 'nivel_curso', 'periodo', 'curso_gratuito',
            'num_vagas',
            'possui_acessabilidade')
