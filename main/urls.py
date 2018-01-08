from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # curso
    url(r'^curso/list$', views.CursosListView.as_view(), name='curso_list'),
    url(r'^curso/(?P<pk>\d+)/$', views.CursosDetailView.as_view(),
        name='curso_detail'),
    url(r'^curso/new/$', views.curso_new, name='curso_new'),
    url(r'^curso/(?P<pk>\d+)/edit/$', views.curso_edit, name='curso_edit'),
    # ies
    url(r'^ies/list/$', views.IESListView.as_view(), name='ies_list'),
    url(r'^ies/(?P<pk>\d+)/$', views.IESDetailView.as_view(),
        name='ies_detail'),
    url(r'^ies/(?P<pk>\d+)/edit/$', views.IESUpdateView.as_view(),
        name='ies_edit'),
    # map
    url(r'^mapa/$', views.map_view, name='map_view'),
]
