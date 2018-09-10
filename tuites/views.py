from django.shortcuts import render
from tuites.models import Tuite
from django.shortcuts import redirect
from django.views.generic import CreateView, RedirectView
from django.urls import reverse_lazy
from tuites.forms import PostTuiteForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
#Lazy é que não vai ser chamado até realmente ser chamado, quando botou só reverse, 
#quando o django ia rodar e ia criar nossas views o django ele percorre nossas views todinhas e ve se tem algum problema 
#e quando ele chegar no reverse ele vai tentar chamar o reverse, ficando em um loop

# Create your views here.


class PostTuiteView(LoginRequiredMixin, CreateView): #É estilo de código do python colocar 2 linhas acima e abaixo das classes
    model = Tuite
    template_name = 'post_tuite.html'
    #fields = ('content', ) #quando há apenas um só elemento precisa colocar a vírgula para não iterar na string
    form_class = PostTuiteForm
    success_url = reverse_lazy('tuites:postar')

    def get_initial(self): #para setar valores default nos campos do form
        return {
            'user': self.request.user
        }
    
    def form_valid(self, form):
        messages.success(
            self.request,
            'Você postou um Tuite!'
        )
        return super().form_valid(form)

class LikeTuiteView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        from_url = self.request.META.get('HTTP_REFERER')
        tuite_pk = kwargs.get('pk')
        user = self.request.user

        tuite = Tuite.objects.get(pk=tuite_pk)
        if tuite.liked_by.filter(pk=user.pk).exists():
            tuite.liked_by.remove(user)
        else:
            tuite.liked_by.add(user)
        #return f'{from_url}#{tuite_pk}' Pode ser usado para abrir uma nova tela com o tuirer curtido, ou trabalhar com alguma outra url
        return f'{from_url}'

#Código não utilizado atualmente
def post_tuite(request):
    context = {}
    if request.method == 'POST':
        print('Enviando formulário!')
        #print(request.POST)
        content = request.POST.get('content', None)
        if content.isspace() or content == '':
            print('Tuite não pode estar vazio!')
            context['error'] = 'Tuite não pode estar vazio!'
        else:
            print('Formulário válido, postar!')
            tuite = Tuite.objects.create(
                content = content,
                author = request.user,
            )
            context['sucess_message'] = f'Seu Tuite de conteúdo "{tuite.content}" foi postado com sucesso!'
        #return redirect('/postar/') funciona, porém apaga o contexto
    return render(request, 'post_tuite.html', context)