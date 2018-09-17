# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.crypto import get_random_string
from django.db import models
from django.utils.crypto import get_random_string

class UserManager(models.Manager):
    def createUser(self):
        return self.create(name= get_random_string(length=8)).id


class User(models.Model):
    name = models.CharField(max_length=255)
    objects = UserManager()

class ArtistManager(models.Manager):
    def createArtist(self, postData):
        Artist.objects.create(
            name=postData['name']
        )

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    objects = ArtistManager()

    
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, related_name="songs")
    liked_users = models.ManyToManyField(User, related_name = 'liked_songs')

    def __repr__(self):
        return "{} {}".format(self.title, self.id)