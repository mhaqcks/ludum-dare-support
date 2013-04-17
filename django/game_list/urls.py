from django.conf.urls import patterns, url
from game_list import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^status/$', views.status, name='status'),
    url(r'^download/$', views.download, name='download'),
    url(r'^games/$', views.games, name='games'),
    url(r'^retrieve_game/$', views.retrieve_game, name='retrieve_game'),
    url(r'^gadget/$', views.gadget, name='gadget'),
    url(r'^build_game/$', views.build_game, name='build_game'),
)
