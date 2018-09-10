from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, RedirectView
from users.models import User
from django.urls import reverse_lazy
from users.mixins import ProfileAccessMixin
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import UserSignupForm

# Create your views here.
class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile' #muda o nome do model a ser puxado no html


class ProfileEditView(ProfileAccessMixin, UpdateView):
    model = User
    fields = ('picture', 'username')
    template_name = 'profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.pk])

class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    pass

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('tuites:postar')

class FollowUserView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        from_url = self.request.META.get('HTTP_REFERER')
        user_pk = kwargs.get('pk')
        user_logado = self.request.user

        user = User.objects.get(pk=user_pk)
        if user_logado.following.filter(pk=user_pk).exists():
            user_logado.following.remove(user)
        else:
            user_logado.following.add(user)
        return f'{from_url}'

class FollowersUserView(DetailView):
    model = User
    template_name = 'followers.html'
    context_object_name = 'userFollower'

    def get_context_data(self, **kwargs):
        context = super(FollowersUserView, self).get_context_data(**kwargs)
        context['followers'] = self.object.seguidores.all()
        return context
