from django.conf.urls import patterns, include, url
from game_list import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^status/$', views.status, name='status'),
    url(r'^download/$', views.download, name='download'),
    url(r'^games/$', views.games, name='games'),
)
