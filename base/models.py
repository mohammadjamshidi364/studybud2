from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(null=True , blank=True , default="/static/images/avatar.svg")
    bio = models.TextField(null=True , blank=True)
    
    def __str__(self):
        return self.username

# class Topics(models.Model):
#     name = models.CharField(max_length=500)

# class Room():
#     host = models.ForeignKey(User , on_delete=models.CASCADE)
#     topic = models.ForeignKey(Topics , on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#     description = models.TextField(null=True , blank=True)
#     participants = models.ManyToManyField(User , related_name="participants" , blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(ato_now_add=True)


# class Message():
#     user = models.ForeignKey(User , on_delete=models.CASCADE)
#     room = models.ForeignKey(Room , on_delete=models.CASCADE)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
    