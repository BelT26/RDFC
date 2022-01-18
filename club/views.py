from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ClubMember, Match, MatchPlayer
from .forms import MatchForm

# Create your views here.


def index(request):
    """returns a view of the home page"""
    return render(request, 'club/index.html')


def members(request):
    """only accessible if a user is logged in.
    returns a view containing details of team and playerscores,
    the next match fixture and a booking form with which the
    club member can book a place in the next match"""
    player = request.user
    league_table = ClubMember.objects.all().order_by('-points')
    fixture_added = False
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


def next_fixture(request):
    member = request.user
    match_players = MatchPlayer.objects.all()
    if member in match_players:
        member.playing_match = True
    try:
        next_fixture = Match.objects.get(next_fixture=True)
    except:
        next_fixture = Match.objects.all().order_by('-match_date')[0]
    return render(request, 'club/next_fixture.html', {
        'next_fixture': next_fixture,
        'member': member
    })

def league_table(request):
    member = request.user
    league_table = ClubMember.objects.all().order_by('-points')
    return render(request, 'club/league_table.html', {
        'league_table': league_table,
        'current_member': member,
    })



def allocate_teams():
    team_members = ClubMember.objects.filter(is_in_team=True)
    scored_players = team_members.order_by('-points')
    sorted_players = scored_players.order_by('played')
    blues.append(sorted_players[0]) 
    for player in blues: 
        messages.success(request, f'blues: {player.first_name}')
        whites.append(sorted_players[1])
    for player in whites:
        messages.success(request, f'whites {player.first_name}')
        messages.success(request, 'teams allocated')


def book_match_place(request):
    player = request.user
    player.is_available = True
    player.save()
    if len(available_players) < 2:
        player.is_in_team = True
        player.save()
        available_players.append(player)
        messages.success(request, 'You have been allocated a place in '
                                  'the next match!')
        if len(available_players) == 2:
            team_members = ClubMember.objects.filter(is_in_team=True)
            scored_players = team_members.order_by('-points')
            sorted_players = scored_players.order_by('played')
            blues.append(sorted_players[0]) 
            for player in blues: 
                messages.success(request, f'blues: {player.first_name}')
            whites.append(sorted_players[1])
            for player in whites:
                messages.success(request, f'whites {player.first_name}')
            messages.success(request, 'teams allocated')
    else:
        reserves.append(player)
        messages.warning(request, 'Unfortunately there is no room '
                                  'on the team. You are reserve '
                                  f'number {len(reserves)}.')                                
    return HttpResponseRedirect(reverse('members'))


def cancel_match_place(request):
    player = request.user
    player.is_available = False
    #available_players.remove(player)
    player.save()
    if player.is_in_team == True:
        player.is_in_team == False
        if len(reserves) > 0:
            available_players.append(reserves[0])
            allocate_teams()
    messages.success(request, 'Your place has been cancelled')
    return HttpResponseRedirect(reverse('members'))





def applications(request):
    """ returns a template showing any pending applications and
    gives the manager the opportunity to approve them """
    pending_applications = ClubMember.objects.filter(is_approved=False)
    current_members = ClubMember.objects.filter(is_approved=True)
    return render(request, 'club/applications.html', {
        'pending_applications':pending_applications,
        'current_members': current_members
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
    return render(request, 'club/add_fixture.html', {
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
    members = ClubMember.objects.filter(is_approved=True)
    member_email_addresses = []
    for member in members:
        member_email_addresses.append(member.email)
    send_mail('Registrations Open!',
              f'Registrations for {match.match_date} have just opened!'
              ' Visit the club site to book your place.',
              'steve@rdfc.com',
               member_email_addresses)
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
    send_mail('Application approved',
              'Congratulations! '
              'Your application to join RDFC has been approved.'
              'We look forward to seeing you!', 
              'steve@rdfc.com',
              (member.email,))
    return HttpResponseRedirect(reverse('applications'))



def reject_member(request, pk):
    queryset = ClubMember.objects.filter(is_approved=False)
    member = get_object_or_404(queryset, id=pk)
    messages.success(request, 'Application rejected')
    send_mail('Application rejected',
              'Sorry. Your application to join RDFC has not been approved'
              'Please contact steve@rdfc for further information',
              'steve@rdfc.com',
              (member.email,))
    return HttpResponseRedirect(reverse('applications'))


def delete_member(request, pk):
    queryset = ClubMember.objects.filter(is_approved=True)
    member = get_object_or_404(queryset, id=pk)
    messages.success(request, 'Member deleted')
    member.delete()
    return HttpResponseRedirect(reverse('applications'))



