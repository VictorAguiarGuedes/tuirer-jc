from django.urls import path
from tuites.views import PostTuiteView, LikeTuiteView

app_name = 'tuites'

urlpatterns = [
    #path('postar/', post_tuite, name="postar"),
    path('postar/', PostTuiteView.as_view(), name="postar"),
    path('like/<int:pk>/', LikeTuiteView.as_view(), name="like"),
]

#tuites(app_label):profile(name)