from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members', views.members, name='members'),
    path('management', views.management, name='management'),
    path('applications', views.applications, name='applications'),
    path('result', views.add_result, name='result'),
    path('fixture', views.add_fixture, name='fixture'),
    path('registrations', views.registrations, name='registrations')
]
