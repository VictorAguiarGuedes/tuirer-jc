from django.shortcuts import render
from django.http import HttpResponse
from core.helpers import get_character_name, ip_info
from datetime import datetime
from tuites.models import Tuite

# Create your views here.
def index(request):
    #import ipdb; ipdb.set_trace()
    #nome = get_character_name(6)
    #country = ip_info('country_name')
    #flag = ip_info('flag')
    #flag_image = f'<img src="{flag}" width="120px">'
    
    contexto = {
        'my_name': "Julia",
        'now': datetime.now(),
        'tuites': Tuite.objects.all(),
        'tuitesVisitante': Tuite.objects.all()[:5],
    }
    
    return render(request, 'home.html', contexto)

#   return HttpResponse(
#       f'Olá do <b>{country}</b>! <br>{flag_image}'
#   )