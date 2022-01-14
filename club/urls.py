from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members', views.members, name='members'),
    path('management', views.management, name='management'),
    path('applications', views.applications, name='applications'),
    path('add_match', views.add_match, name='add_match'),
    path('select_match', views.select_match, name='select_match'),
    path('edit_match:<str:pk>', views.edit_match, name='edit_match'),
    path('delete_match:<str:pk>', views.delete_match, name='delete_match'),
    path('registrations', views.registrations, name='registrations'),
    path('book_match_place', views.book_match_place, name='book_match_place')
]
