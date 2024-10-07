from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from datetime import *

class User(AbstractUser):
    username = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def profile(self):
        profile = Profile.objects.get(user=self)
    
    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100, null=True, blank=True)
    middle_name = models.CharField(max_length = 100, null=True, blank=True)
    last_name = models.CharField(max_length = 100, null=True, blank=True)
    bio = models.TextField(null=True, blank = True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
