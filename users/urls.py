from django.urls import path
from users.views import (
    ProfileView, 
    ProfileEditView, 
    UserLoginView,
    UserLogoutView,
    UserSignupView,
    FollowUserView,
    FollowersUserView,
)

app_name = 'users'

urlpatterns = [
    path('perfil/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('perfil/<int:pk>/editar/', ProfileEditView.as_view(), name="profile-edit"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('signup/', UserSignupView.as_view(), name="signup"),
    path('seguir/<int:pk>', FollowUserView.as_view() , name="seguir"),
    path('perfil/<int:pk>/seguidores', FollowersUserView.as_view(), name="seguidores"),
]

#users(app_name):profile(name)