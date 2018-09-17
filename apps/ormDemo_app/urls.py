from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.index),
    url(r'^createArtist$', views.createArtist),
    url(r'^createSong$', views.createSong),
    url(r'^createFavorite/(?P<song_id>\d+)', views.createFavorite),
    url(r'^destroyFavorite/(?P<song_id>\d+)', views.destroyFavorite),
    url(r'^logout$', views.logout)
]
