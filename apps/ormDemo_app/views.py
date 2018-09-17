# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Artist, Song, User

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        request.session['user_id'] = User.objects.createUser()
    me = User.objects.get(id=request.session['user_id'])
    all_songs = Song.objects.all()
    favorites = me.liked_songs.all()
    not_favorites = all_songs.difference(favorites)
    context = {
        'all_songs' : all_songs,
        'all_artists': Artist.objects.all(),
        'user' : me,
        'favorites': favorites, 
        'not_favorites': not_favorites
    }
    return render(request, 'ormDemo_app/index.html', context)

def createArtist(request):
    # Artist.objects.createArtist(request.POST)
    Artist.objects.create(
        name=request.POST['name']
    )
    return redirect('/')

def createSong(request):
    Song.objects.create(
        title=request.POST['title'],
        artist=Artist.objects.get(name=request.POST['artist'])
    )
    return redirect('/')

def createFavorite(request, song_id):
    me = User.objects.get(id=request.session['user_id'])
    song = Song.objects.get(id=song_id)
    song.liked_users.add(me)
    song.save()
    return redirect('/')

def destroyFavorite(request, song_id):
    me = User.objects.get(id=request.session['user_id'])
    song = Song.objects.get(id=song_id)
    song.liked_users.remove(me)
    song.save()
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')






    #    'all_artists':Artist.objects.all(),
    #     'user' : User.objects.get(id = request.session['user_id']),
    #     'favorites': Song.objects.filter(liked_users=User.objects.get(id=request.session['user_id'])),
    #     'not_favorites':Song.objects.exclude(liked_users=User.objects.get(id=request.session['user_id']))