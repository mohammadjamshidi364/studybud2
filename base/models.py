from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(null=True , blank=True , default="/static/images/avatar.svg")
    bio = models.TextField(null=True , blank=True)
    
    def __str__(self):
        return self.username

class Topics(models.Model):
    name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    topic = models.ForeignKey(Topics , on_delete=models.SET_NULL, null=True )
    name = models.CharField(max_length=250)
    description = models.TextField(null=True , blank=True)
    participants = models.ManyToManyField(User , related_name="participants" , blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-updated' , '-created']


class Message(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    room = models.ForeignKey(Room , on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]