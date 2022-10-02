from enum import auto
from heapq import nlargest
from operator import mod
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from turtle import update
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) # the users currently active in the room
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created'] # newest updated item should come first
    
    def __str__(self):
        return str(self.name)
    
    
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # on delete -> CASCADE = delete all children 
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]