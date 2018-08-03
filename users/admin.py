from django.contrib import admin
from users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('following', )
    fieldsets = (
        ('Dados pessoais', {
            'fields': ('username', 'email', 'date_joined'),
            'classes': ('wield', ) #Agora pode estilizar o django com essa classe
        }),
        ('Tuiter', {
            'fields': ('following', ),
            'description': 'Coisas relacionadas ao nosso sistema'
        })
    )

admin.site.register(User, UserAdmin)

    # fieldsets = (
    #     ('Dados pessoais', {
    #         'fields': (
    #             ('username', 'email'),
    #             'date_joined')
    #     }),
    # )