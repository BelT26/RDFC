from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next_fixture', views.next_fixture, name='next_fixture'),
    path('league_table', views.view_league_table, name='league_table'),
    path('results', views.results, name='results'),
    path('booking_form', views.booking_form, name='booking_form'),
    path('confirm_availability', views.confirm_availability,
         name='confirm_availability'),
    path('member_admin', views.member_admin, name='member_admin'),
    path('add_match', views.add_match, name='add_match'),
    path('select_match', views.select_match, name='select_match'),
    path('edit_match:<str:pk>', views.edit_match, name='edit_match'),
    path('add_score:<str:pk>', views.add_score, name='add_score'),
    path('delete_score:<str:pk>', views.delete_score, name='delete_score'),
    path('delete_match:<str:pk>', views.delete_match, name='delete_match'),
    path('cancel_match_place', views.cancel_match_place,
         name='cancel_match_place'),
    path('open_reg:<str:pk>', views.open_reg, name='open_reg'),
    path('close_reg:<str:pk>', views.close_reg, name='close_reg'),
    path('add_next:<str:pk>', views.add_next, name='add_next'),
    path('remove_next:<str:pk>', views.remove_next, name='remove_next'),
    path('allocate_teams:<str:pk>', views.allocate_teams,
         name='allocate_teams'),
    path('reset_teams:<str:pk>', views.reset_teams, name='reset_teams'),
    path('approve_member:<str:pk>', views.approve_member,
         name='approve_member'),
    path('delete_member:<str:pk>', views.delete_member, name='delete_member'),
    path('see_players:<str:pk>', views.see_players, name='see_players')
]
