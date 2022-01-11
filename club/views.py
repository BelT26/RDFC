from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import ClubMember, Match


# Create your views here.


def index(request):
    """returns a view of the home page"""
    return render(request, 'club/index.html')


available_players = []
reserves = []
blues = []
whites = []


def members(request):
    """only accessible if a user is logged in.
    returns a view containing details of team and playerscores,
    the next match fixture and a booking form with which the
    club member can book a place in the next match"""
    league_table = ClubMember.objects.all().order_by('-points')
    next_fixture = Match.objects.all().order_by('-match_date')[0]
    all_matches = Match.objects.all().order_by('-match_date')
    past_results = all_matches[1:]
    registrations_open = True
    if len(available_players) > 11:
        registrations_open = False
    context = {
        'league_table': league_table,
        'next_fixture': next_fixture,
        'past_results': past_results,
        'registrations_open': registrations_open
    }
    return render(request, 'club/members.html', context)


def management(request):
    """returns a list of management functions"""
    return render(request, 'club/management.html')


def applications(request):
    """ returns a template showing any pending applications and
    gives the manager the opportunity to approve them """
    return render(request, 'club/applications.html')


def add_fixture(request):
    """returns a form in which the manager can add, remove
    or modify a match fixture"""
    return render(request, 'club/fixture.html')


def add_result(request):
    """returns a form in which the manager can add, remove
    or modify a match result"""
    return render(request, 'club/result.html')


def registrations(request):
    """returns a form in which the manager can open or
    or close registrations for the next match"""
    return render(request, 'club/registrations.html')


def book_match_place(request):
    """allows club members to book a place on the team
    for the next match. If teams are full the player is
    placed on a reserve list"""
    player = None
    if request.user.is_authenticated():
        player = request.user
        if len(available_players) <= 12:
            player['is_in_team'] = True
            available_players.append(player)
            messages.success(request, 'You have been allocated a place in '
                                      'the next match!')
        else:
            reserves.append(player)
            messages.warning(request, 'Unfortunately there is no room on '
                                      'the team')
            messages.warning(request, f'You are reseve number {len(reserves)}.')
    return HttpResponseRedirect(reverse('members'))
