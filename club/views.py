from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import ClubMember, Match
from .forms import MatchForm
from . import helpers


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
    player = request.user
    league_table = ClubMember.objects.all().order_by('-points')
    try:
        next_fixture = Match.objects.get(next_fixture=True)
    except:
        next_fixture = Match.objects.all().order_by('-match_date')[0]
    all_matches = Match.objects.all().order_by('-match_date')
    past_results = all_matches[1:]
    registrations_open = True
    if len(available_players) > 11:
        registrations_open = False
    context = {
        'player': player,
        'league_table': league_table,
        'next_fixture': next_fixture,
        'past_results': past_results,
        'registrations_open': registrations_open,
        'blues': blues,
        'whites': whites,
        'reserves': reserves
    }
    return render(request, 'club/members.html', context)


def management(request):
    """returns a list of management functions"""
    return render(request, 'club/management.html')


def applications(request):
    """ returns a template showing any pending applications and
    gives the manager the opportunity to approve them """
    pending_applications = ClubMember.objects.filter(is_approved=False)
    return render(request, 'club/applications.html', {
        'pending_applications':pending_applications
    })


def add_match(request):
    """returns a form in which the manager can add, remove
    or modify a match fixture"""
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = Match(
                match_date=form.cleaned_data['match_date'],
                time=form.cleaned_data['time'],
                location=form.cleaned_data['location'],
                blue_goals=form.cleaned_data['blue_goals'],
                white_goals=form.cleaned_data['white_goals'],
                results_added=form.cleaned_data['results_added']
            )
            match.save()
            messages.success(request, 'Match successfully added')
            return HttpResponseRedirect(reverse('index'))
    form = MatchForm()
    return render(request, 'club/fixture.html', {
        'form': form
    })


def select_match(request):
    matches = Match.objects.all().order_by('-match_date')
    return render(request, 'club/matches.html', {
        'matches': matches
    })


def edit_match(request, pk):
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    form = MatchForm(instance=match)
    
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            match = Match(
                match_date=form.cleaned_data['match_date'],
                time=form.cleaned_data['time'],
                location=form.cleaned_data['location'],
                blue_goals=form.cleaned_data['blue_goals'],
                white_goals=form.cleaned_data['white_goals'],
                results_added=form.cleaned_data['results_added']
            )
            match.save()
            messages.success(request, 'Match successfully updated')
            return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'club/fixture.html', {
        'form': form
    })


def delete_match(request, pk):
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    match.delete()
    messages.success(request, 'Match successfully deleted')
    return HttpResponseRedirect(reverse('select_match'))


def add_next(request, pk):
    """checks that there is not already a match flagged as
    the next fixture. Displays an error message if there is
    otherwise changes the next_fixture property of the match
    to true and updates the display in members.html"""
    next_match = Match.objects.filter(next_fixture=True)
    if len(next_match) > 0:
        messages.error(request, 'Only one match can be flagged as the next fixture')
        messages.error(request, 'Please remove the next fixture flag from the current match')
        return HttpResponseRedirect(reverse('select_match'))
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    match.next_fixture = True
    match.save()        
    messages.success(request, 'Next fixture updated')
    return HttpResponseRedirect(reverse('select_match'))


def remove_next(request, pk):
    queryset = Match.objects.filter(next_fixture=True)
    match = get_object_or_404(queryset, id=pk)
    match.next_fixture = False
    match.save()
    messages.success(request, 'Next fixture flag removed')
    return HttpResponseRedirect(reverse('select_match'))


def open_reg(request, pk):
    open_matches = Match.objects.filter(registrations_open=True)
    if len(open_matches) > 0:
        messages.error(request, 'Registrations can only be '
                                'open for one match at a time. '
                                'Please close registrations for any '
                                'open match before proceding.')
        return HttpResponseRedirect(reverse('select_match'))
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    match.registrations_open = True
    match.save()
    messages.success(request, "Registrations opened")
    return HttpResponseRedirect(reverse('select_match'))


def close_reg(request, pk):
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    match.registrations_open = False
    match.save()
    messages.success(request, f"Registrations closed")
    return HttpResponseRedirect(reverse('select_match'))


def approve_member(request, pk):
    queryset = ClubMember.objects.filter(is_approved=False)
    member = get_object_or_404(queryset, id=pk)
    member.is_approved = True
    member.save()
    messages.success(request, 'Application approved')
    pending_applications = ClubMember.objects.filter(is_approved=False)
    return HttpResponseRedirect(reverse('applications'))


# def book_match_place(request):
#     """allows club members to book a place on the team
#     for the next match. If teams are full the player is
#     placed on a reserve list"""
#     player = None
#     if request.user.is_authenticated():
#         player = request.user
#         if len(available_players) <= 12:
#             player['is_in_team'] = True
#             available_players.append(player)
#             messages.success(request, 'You have been allocated a place in '
#                                       'the next match!')
#         else:
#             reserves.append(player)
#             messages.warning(request, 'Unfortunately there is no room on '
#                                       'the team')
#             messages.warning(request, f'You are reseve number {len(reserves)}.')
#     return HttpResponseRedirect(reverse('members'))

def book_match_place(request):
    player = request.user
    player.is_available = True
    player.save()
    if len(available_players) < 12:     
        available_players.append(player)
        messages.success(request, 'You have been allocated a place in '
                                  'the next match!')
        # for player in available_players: 
        # messages.success(request, f'available players {player.first_name}')
        # if len(available_players) == 12:
        #     allocate_teams()
    else:
        reserves.append(player)
        messages.warning(request, 'Unfortunately there is no room '
                                  'on the team. You are reserve '
                                  f'number {len(reserves)}.')                                
    return HttpResponseRedirect(reverse('members'))


def cancel_match_place(request):
    player = request.user
    if player in blues:
        blues.remove(player)
    elif player in whites:
        whites.remove(player)
    elif player in reserves:
        reserves.remove(player)
    elif player in available_players:
        available_players.remove(player)
    player.is_available = False
    player.save()
    messages.success(request, 'Your place has been cancelled')
    #allocate_teams()
    return HttpResponseRedirect(reverse('members'))
