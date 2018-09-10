from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    picture = models.ImageField('Foto de perfil', default='img/blank-profile-picture.png')
    following = models.ManyToManyField('self', related_name="seguidores", symmetrical=False, blank=True)

    @property
    def followers_count(self):
        return self.seguidores.count()