from django.contrib import admin
from tuites.models import Tuite
from users.models import User


# Register your models here.
class TuiteAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date_created')
    list_display = ('content', 'author', 'date_created')

admin.site.register(Tuite, TuiteAdmin)