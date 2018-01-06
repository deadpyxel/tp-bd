from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^curso/(?P<pk>\d+)/$', views.curso_detail, name='curso_detail'),
    url(r'^curso/new/$', views.curso_new, name='curso_new'),
    url(r'^curso/(?P<pk>\d+)/edit/$', views.curso_edit, name='curso_edit'),
]
