from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # URLs curso
    url(r'^curso/$', views.CursoListView.as_view(), name='curso-list'),
    url(r'^curso/(?P<pk>\d+)/$', views.CursoDetailView.as_view(),
        name='curso-detail'),
    url(r'^curso/add/$', views.CursoCreateView.as_view(), name='curso-add'),
    url(r'^curso/(?P<pk>\d+)/edit/$', views.CursoUpdateView.as_view(),
        name='curso-edit'),
    url(r'^curso/(?P<pk>\d+)/delete/$', views.CursoDeleteView.as_view(),
        name='curso-delete'),

    # URLs IES
    url(r'^ies/$', views.IESListView.as_view(), name='ies-list'),
    url(r'^ies/add/$', views.IESCreateView.as_view(), name='ies-add'),
    url(r'^ies/(?P<pk>\d+)/$', views.IESDetailView.as_view(),
        name='ies-detail'),
    url(r'^ies/(?P<pk>\d+)/edit/$', views.IESUpdateView.as_view(),
        name='ies-edit'),
    url(r'^ies/(?P<pk>\d+)/delete$', views.IESDeleteView.as_view(),
        name='ies-delete'),

    # URLs Mapa
    url(r'^mapa/$', views.map_view, name='map-view'),
]
