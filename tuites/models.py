from django.db import models
from tuites.managers import TuitesManager

# Create your models here.
class Tuite(models.Model):
    content = models.CharField('Tuite', max_length=280)
    author = models.ForeignKey(
        'users.User',
        on_delete = models.CASCADE, #models.PROTECT protege da exclusão, e impede excluir o usuário até excluir os tuites
        related_name = 'tuites' #Permite chamar a partir do model de User os tuites que se relacionam com ele    
    )
    date_created = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField('users.User', blank = True)

    @property
    def likes_count(self):
        return self.liked_by.count() 

    objects = TuitesManager() #Sobrescrevendo o atributo objects para nosso manager criado, mas como herança, apenas herdando e colocando a mais

    def __str__(self):
        return f'{self.author.username}: {self.content}'

    class Meta:
        ordering = ('-date_created', )

#default = 1, on_delete = models.SET_DEFAULT Seta um valor default na criação do campo, nesse caso passando a pk do user