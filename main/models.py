from django.utils import timezone

from django.db import models


# TODO Adicionar endereço da instituicao
class IntituicaoEnsinoSuperior(models.Model):
    # Organizacao Academica
    UNIVERSIDADE = 'UNI'
    CENTRO_UNIVERSITARIO = 'CENT_UNI'
    FACULDADE = 'FACUL'
    INTITUTO_FEDERAL = 'INST_FED'
    ORG_ACADEMICA_CHOICES = (
        (UNIVERSIDADE, 'Universidade'),
        (CENTRO_UNIVERSITARIO, 'Centro Universitário'),
        (FACULDADE, 'Faculdade'),
        (INTITUTO_FEDERAL, 'Instituto Federal'),
    )

    # Categoria administrativa
    REDE_PUBLICA = 'PUB'
    REDE_PRIVADA = 'PRI'
    REDE_CHOICES = (
        (REDE_PUBLICA, 'Pública'),
        (REDE_PRIVADA, 'Privada'),
    )
    ADM_FEDERAL = 'FED'
    ADM_ESTADUAL = 'EST'
    ADM_MUNICIPAL = 'MUN'
    ADM_PRIVADA = 'PRI'
    DEPARTAMENTO_ADM_CHOICES = (
        (ADM_FEDERAL, 'Federal'),
        (ADM_ESTADUAL, 'Estadual'),
        (ADM_MUNICIPAL, 'Municipal'),
        (ADM_PRIVADA, 'Privada'),
    )

    nome_IES = models.CharField('Nome', max_length=100, null=False)
    sigla_IES = models.CharField('Sigla', max_length=10, null=False)
    email_IES = models.CharField('Email', max_length=32, null=False)
    cod_mant = models.ForeignKey('Mantenedora', on_delete=models.CASCADE,
                                 default=1)
    organizacao_academica = models.CharField('Organização Acadêmica',
                                             max_length=10,
                                             choices=ORG_ACADEMICA_CHOICES,
                                             default=UNIVERSIDADE, null=False)
    rede = models.CharField('Rede', max_length=3, choices=REDE_CHOICES,
                            default=REDE_PUBLICA, null=False)
    departamento_administrativo = models.CharField(
        'Departamento Administrativo', max_length=3,
        choices=DEPARTAMENTO_ADM_CHOICES, default=ADM_ESTADUAL, null=False)
    cep = models.IntegerField('CEP', default=00000000, null=False)

    def __str__(self):
        return self.nome_IES


class Mantenedora(models.Model):
    nome_mant = models.CharField('Nome', max_length=80, null=False)

    def __str__(self):
        return self.nome_mant


# TODO Adicionar endereço onde o curso é ofertado
class Curso(models.Model):
    # Modalidades possiveis para o curso
    PRESENCIAL = 'PRE'
    EAD = 'EAD'
    MODALIDADE_CHOICES = (
        (PRESENCIAL, 'Presencial'),
        (EAD, 'Ensino à distância'),
    )

    # Nivel do curso
    BACHARELADO = 'BACH'
    LICENCIATURA = 'LICEN'
    TECNICO = 'TEC'
    NAO_APLICAVEL = 'NAP'
    NIVEL_CHOICES = (
        (BACHARELADO, 'Bacharelado'),
        (LICENCIATURA, 'Licenciatura'),
        (TECNICO, 'Técnico'),
        (NAO_APLICAVEL, 'Não Aplicável'),
    )

    # Periodo do curso
    MATUTINO = 'M'
    VESPERTINO = 'V'
    NOTURNO = 'N'
    INTEGRAL = 'I'
    VESPERTINO_NOTURNO = 'VN'
    PERIODO_CHOICES = (
        (MATUTINO, 'Matutino'),
        (VESPERTINO, 'Vespertino'),
        (NOTURNO, 'Noturno'),
        (INTEGRAL, 'Integral'),
        (VESPERTINO_NOTURNO, 'Vespertino/Noturno'),
    )

    nome_curso = models.CharField('Nome do Curso', max_length=200, null=False)
    data_inicio_oferta = models.DateField('Data de início da oferta',
                                          default=timezone.now, null=False)
    cod_IES = models.ForeignKey('IntituicaoEnsinoSuperior', on_delete=models.CASCADE,
                                 default=1)
    carga_horaria = models.IntegerField('Carga Horária', default=2400,
                                        null=False)
    modalidade = models.CharField(max_length=3, choices=MODALIDADE_CHOICES,
                                  default=PRESENCIAL, null=False)
    nivel_curso = models.CharField(max_length=5, choices=NIVEL_CHOICES,
                                   default=BACHARELADO, null=False)
    periodo = models.CharField(max_length=2, choices=PERIODO_CHOICES,
                               default=NOTURNO, null=False)
    curso_gratuito = models.BooleanField('Curso Gratuito', default=True)
    num_vagas = models.IntegerField('Número de vagas', default=40, null=False)
    possui_acessabilidade = models.BooleanField('Possui Acessabilidade',
                                                default=False)

    def __str__(self):
        return self.nome_curso
