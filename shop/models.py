from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Developer(models.Model):
    
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


class Game(models.Model):
    title    = models.CharField(max_length=30, null=False, blank=False, unique=False)
    price    = models.FloatField(null=False, blank=False, unique=False)

    def __str__(self):
        return self.title
