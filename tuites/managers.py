from django.db import models


class TuitesManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(content__icontains=query) |
            models.Q(author__username__icontains=query)
        )

#Com o Q ṕermite fazer várias buscas, independente do parâmetro que você estiver buscando, pode usar o | ou $

#QuerySet | Managers

#icontains
# i - significa insensitive case
#contains - verifica se contém a palavra Sou


#palavras = ['pai', 'Sou lindo']
#Tuite.objects.filter(content_in=palavras)

#eu = User.objects.get(pk=1)
#Tuite.objects.create(content='Qualquer coisa', author=eu)