from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members', views.members, name='members'),
    path('social', views.social, name='social'),
    path('signup', views.signup, name='signup'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('login', views.login, name='login'),
]
