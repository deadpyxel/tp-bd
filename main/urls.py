from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # URLs curso
    url(r'^curso/$', views.CursosListView.as_view(), name='curso-list'),
    url(r'^curso/(?P<pk>\d+)/$', views.CursosDetailView.as_view(),
        name='curso-detail'),
    url(r'^curso/add/$', views.curso_new, name='curso-add'),
    url(r'^curso/(?P<pk>\d+)/edit/$', views.curso_edit, name='curso-edit'),
    url(r'^curso/(?P<pk>\d+)/delete/$', views.CursoDeleteView.as_view(),
        name='curso-delete'),

    # URLs IES
    url(r'^ies/$', views.IESListView.as_view(), name='ies-list'),
    url(r'^ies/(?P<pk>\d+)/$', views.IESDetailView.as_view(),
        name='ies-detail'),
    url(r'^ies/(?P<pk>\d+)/edit/$', views.IESUpdateView.as_view(),
        name='ies-edit'),
    url(r'^ies/(?P<pk>\d+)/delete$', views.IESDeleteView.as_view(),
        name='ies-delete'),

    # URLs Mapa
    url(r'^mapa/$', views.map_view, name='map-view'),
]
