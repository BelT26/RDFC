from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .models import ClubMember, Match, MatchPlayer
from .forms import MatchForm, ResultsForm


# Create your views here.
def index(request):
    """Returns a view of the home page"""
    return render(request, 'club/index.html')


@login_required
def next_fixture(request):
    """
    Checks which match has been flagged as the next fixture
    and passes its details to the next fixture template. If no
    match has been flagged the latest match in the database is
    retrieved to avoid an error being thrown. Checks whether the
    current user is already registered for the match and passes
    this information to the template. If teams have been allocated
    passes collect the details to be displayed on the template
    """
    member = request.user
    if Match.objects.filter(next_fixture=True).count() > 0:
        next_game = Match.objects.get(next_fixture=True)
    else:
        next_game = Match.objects.all().order_by('-match_date')[0]
    blues = MatchPlayer.objects.filter(team='blue', match_id=next_game)
    whites = MatchPlayer.objects.filter(team='white', match_id=next_game)
    reserves = MatchPlayer.objects.filter(reserve=True, match_id=next_game)
    return render(request, 'club/next_fixture.html', {
        'next_game': next_game,
        'member': member,
        'blues': blues,
        'whites': whites,
        'reserves': reserves
    })


@login_required
def view_league_table(request):
    """ Calculates and updates the number of wins, draws and losses for each
    approved memeber. Sorts all members in descending order according to
    their points, then in ascending order according to the number of matches
    they have played. Returns a view of the resulting table in which the
    current user's own results are highlighted """
    current_member = request.user
    all_members = ClubMember.objects.filter(is_approved=True)
    for member in all_members:
        member.won = MatchPlayer.objects.filter(player_id=member.id,
                                                win=True).count()
        member.drawn = MatchPlayer.objects.filter(player_id=member.id,
                                                  draw=True).count()
        member.lost = MatchPlayer.objects.filter(player_id=member.id,
                                                 loss=True).count()
        member.played = MatchPlayer.objects.filter(player_id=member.id,
                                                   played=True).count()
        member.points = (member.won * 3) + member.drawn
        member.save()
    league_table = ClubMember.objects.filter(
                                             is_approved=True).order_by(
                                             '-points', 'played')
    return render(request, 'club/league_table.html', {
        'league_table': league_table,
        'current_member': current_member,
    })


@login_required
def results(request):
    """Returns a view displaying a table with the scores for
    all matches that the manager has added the result for """
    past_results = Match.objects.filter(results_added=True)
    for match in past_results:
        match.blueteam = []
        blue_players = MatchPlayer.objects.filter(
                        team='blue', match_id=match)
        for player in blue_players:
            match.blueteam.append(player)
        match.whiteteam = []
        white_players = MatchPlayer.objects.filter(
                            team='white', match_id=match)
        for player in white_players:
            match.whiteteam.append(player)
        match.save()
    return render(request, 'club/results.html', {
        'past_results': past_results
    })


@login_required
def booking_form(request):
    """ Checks whether the manager has opened registrations
    for a match. If so checks whether the player has already
    registered for the match and whether there are any spaces
    remaining. Passes the information to and returns the match
    booking template """
    if Match.objects.filter(registrations_open=True).exists():
        match = Match.objects.get(registrations_open=True)
        registrations_open = True
    else:
        match = Match.objects.all().order_by('-match_date')[0]
        registrations_open = False
    player = request.user
    if MatchPlayer.objects.filter(player_id=player, match_id=match).exists():
        player_registered = True
    else:
        player_registered = False
    match_full = False
    registered_players = MatchPlayer.objects.filter(
                            reserve=False, match_id=match)
    if registered_players.count() == 12:
        match_full = True
    return render(request, 'club/match_booking.html', {
        'player_registered': player_registered,
        'match': match,
        'registrations_open': registrations_open,
        'match_full': match_full,
    })


@login_required
def confirm_availability(request):
    """ Allows the user to register their availability for the
    next match. Checks how many players have already registered.
    If the maximum number of players has not been reached,
    the player is allocated a space on the team and is informed
    of this via a success message. If the teams are full the
    player is placed on a reserve list and informed of their
    position on the list via message. New MatchPlayer instances
    are created in both instances with the 'reserve' property
    set to True or False accordingly """
    player = request.user
    match = Match.objects.get(registrations_open=True)
    registered_players = MatchPlayer.objects.filter(match_id=match)
    num_registered_players = registered_players.count()
    if num_registered_players < 12:
        player.save()
        new_player = MatchPlayer(player_id=player, match_id=match)
        new_player.save()
        messages.success(request, 'You have been allocated a place in '
                                  'the next match!')
    else:
        new_player = MatchPlayer(player_id=player, match_id=match,
                                 reserve=True)
        new_player.save()
        reserves = MatchPlayer.objects.filter(reserve=True, match_id=match)
        num_reserves = reserves.count()
        messages.success(request, 'You are number '
                                  f'{num_reserves} on the reserve list')
    return HttpResponseRedirect(reverse('index'))


@login_required
def cancel_match_place(request):
    """ Allows a member who has already registered for a
    match to cancel their booking.  If the member has been
    allocated a place on the team an email is generated to
    the club manager to inform them that they need to
    reallocate the teams """
    player = request.user
    match = Match.objects.get(registrations_open=True)
    match_player = MatchPlayer.objects.get(
                    player_id=player, match_id=match)
    registered_players = MatchPlayer.objects.filter(match_id=match)
    num_registered_players = registered_players.count()
    if match_player.reserve is False and num_registered_players > 11:
        send_mail('Player Cancellation',
                  f'{match_player.player_id} '
                  'has cancelled their place in the next match '
                  'Please reallocate the teams',
                  'management@rdfc.com',
                  ('helen.taylor@hotmail.it',))
    match_player.delete()
    messages.success(request, 'Your place has been cancelled')
    return HttpResponseRedirect(reverse('index'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def member_admin(request):
    """ Returns a template showing any pending applications and
    gives the manager the opportunity to approve or reject them.
    Shows the contact details for existing members and allows
    the manager to remove the member from the club"""
    pending_applications = ClubMember.objects.filter(is_approved=False)
    current_members = ClubMember.objects.filter(is_approved=True)
    return render(request, 'club/member_admin.html', {
        'pending_applications': pending_applications,
        'current_members': current_members
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_match(request):
    """Returns a form in which the manager can add a new
    match fixture. Shows a success message once the match
    has been added."""
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            match = Match(
                match_date=form.cleaned_data['match_date'],
                time=form.cleaned_data['time'],
                location=form.cleaned_data['location'],
            )
            match.save()
            messages.success(request, 'Match successfully added')
            return HttpResponseRedirect(reverse('select_match'))
        else:
            messages.error(request, 'There was an error on your form')
    form = MatchForm()
    return render(request, 'club/add_fixture.html', {
        'form': form
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def select_match(request):
    """Returns a table with a list of all matches and all
    available admin options for the manager"""
    matches = Match.objects.all().order_by('-match_date')
    return render(request, 'club/matches.html', {
        'matches': matches
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_match(request, pk):
    """Retrieves the data of the selected match and returns
    a form in which the manager can update the time, date
    and location"""
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    form = MatchForm(instance=match)

    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            messages.success(request, 'Match successfully updated')
            return HttpResponseRedirect(reverse('select_match'))
    return render(request, 'club/edit_fixture.html', {
        'match': match,
        'form': form
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_score(request, pk):
    """Returns a results form in which the manager can enter
    the scores of a match. Retrieves all the match players who
    played in the game and updates their win/loss/draw property
    accordingly"""
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    form = ResultsForm(instance=match)
    if request.method == 'POST':
        form = ResultsForm(request.POST, instance=match)
        if form.is_valid():
            match.results_added = True
            form.save()
            all_players = MatchPlayer.objects.filter(match_id=match,
                                                     reserve=False)
            for player in all_players:
                player.played = True
                player.save()
            blues = all_players.filter(team='blue')
            whites = all_players.filter(team='white')
            if match.blue_goals > match.white_goals:
                for player in blues:
                    player.win = True
                    player.save()
                for player in whites:
                    player.loss = True
                    player.save()           
            elif match.white_goals > match.blue_goals:
                for player in blues:
                    player.loss = True
                    player.save()
                for player in whites:
                    player.win = True
                    player.save()
            else:
                for player in all_players:
                    player.draw = True
                    player.save()
            messages.success(request, 'Match scores updated')
            return HttpResponseRedirect(reverse('league_table'))
        else:
            messages.error(request, 'something went wrong')
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'club/add_score.html', {
        'form': form,
        'match': match
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_score(request, pk):
    """Allows the manager to delete the results of a match
    and automatically updates the players' staticstics"""
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    match.results_added = False
    match.blue_goals = 0
    match.white_goals = 0
    match.save()
    all_players = MatchPlayer.objects.filter(match_id=match)
    for player in all_players:
        player.win = False
        player.draw = False
        player.loss = False
        player.save()
    messages.success(request, 'Result deleted')
    return HttpResponseRedirect(reverse('select_match'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_match(request, pk):
    """removes a match from the database"""
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    match.delete()
    messages.success(request, 'Match successfully deleted')
    return HttpResponseRedirect(reverse('select_match'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_next(request, pk):
    """Checks that there is not already a match flagged as
    the next fixture. Displays an error message if there is,
    otherwise changes the next_fixture property of the match
    to true and updates the display in members.html"""
    next_match = Match.objects.filter(next_fixture=True)
    if len(next_match) > 0:
        current_fixture = Match.objects.get(next_fixture=True)
        messages.error(request, 'Only one match can be flagged as the next '
                                'fixture. Please remove the next fixture flag'
                                f'from {current_fixture.match_date}')
        return HttpResponseRedirect(reverse('select_match'))
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    match.next_fixture = True
    match.save()
    messages.success(request, 'Next fixture updated')
    return HttpResponseRedirect(reverse('select_match'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def remove_next(request, pk):
    """Removes the next fixture flag from a match"""
    queryset = Match.objects.filter(next_fixture=True)
    match = get_object_or_404(queryset, id=pk)
    match.next_fixture = False
    match.save()
    messages.success(request, 'Next fixture flag removed')
    return HttpResponseRedirect(reverse('select_match'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def open_reg(request, pk):
    """Checks that there is not already a match which has
    registrations open. Displays an error message if there is,
    otherwise changes the registrations_open property of the match
    to True. Generates an email to all members to advise them
    that match registrations are open."""
    open_matches = Match.objects.filter(registrations_open=True)
    if len(open_matches) > 0:
        open_match = Match.objects.get(registrations_open=True)
        messages.error(request, 'Registrations can only be '
                                'open for one match at a time. '
                                'Please close registrations for  '
                                f'{open_match.match_date} before proceding.')
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


@login_required
@user_passes_test(lambda u: u.is_superuser)
def close_reg(request, pk):
    """Closes the registrations of the selected match"""
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    match.registrations_open = False
    match.save()
    messages.success(request, f"Registrations closed for {match.match_date}")
    return HttpResponseRedirect(reverse('select_match'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def see_players(request, pk):
    """Returns a template showing all members who have a
    confirmed place on the next match and those on the
    reserve list"""
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    players = MatchPlayer.objects.filter(reserve=False, match_id=match)
    reserves = MatchPlayer.objects.filter(reserve=True,
                                          match_id=match).order_by(
                                          'registration_time')
    return render(request, 'club/see_players.html', {
        'players': players,
        'reserves': reserves,
        'match': match,
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def allocate_teams(request, pk):
    """Checks whether 12 people have confirmed places for
    the match. If not checks the reserve list and pulls in
    the player who registerd first. If there are no reserves
    the manager is alerted that he needs 12 people before he
    can allocate teams.  If there are 12 confirmed members they
    are sorted by their points, matches played and username and
    allocated teams according to their position"""
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    registered_players = MatchPlayer.objects.filter(match_id=match,
                                                    reserve=False)
    reserves = MatchPlayer.objects.filter(match_id=match,
                                          reserve=True).order_by(
                                          'registration_time')
    while registered_players.count() < 12:
        if reserves.count() > 0:
            reserve_selected = reserves[0]
            reserve_selected.reserve = False
            reserve_selected.save()
            registered_players = MatchPlayer.objects.filter(match_id=match,
                                                            reserve=False)
        else:
            messages.error(request, 'You require 12 available '
                                    'members to allocate teams')
            return HttpResponseRedirect(reverse('select_match'))
    reserves = MatchPlayer.objects.filter(match_id=match, reserve=True)
    blue_indices = [0, 3, 5, 7, 9, 11]
    white_indices = [1, 2, 4, 6, 8, 10]
    ordered_players = MatchPlayer.objects.filter(
                                                 match_id=match,
                                                 reserve=False).order_by(
                                                 '-player_id__points',
                                                 'player_id__played',
                                                 'player_id__username')
    for i in blue_indices:
        blue = ordered_players[i]
        blue.team = 'blue'
        blue.save()
    for i in white_indices:
        white = ordered_players[i]
        white.team = 'white'
        white.save()
    messages.success(request, "Teams allocated")
    match.teams_allocated = True
    match.save()
    return HttpResponseRedirect(reverse('select_match'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def reset_teams(request, pk):
    """Sets the team property of all confirmed players back
    to None. Used by the manager if a confirmed player cancels
    their place and they need to allocate teams again"""
    queryset = Match.objects.all()
    match = get_object_or_404(queryset, id=pk)
    registered_players = MatchPlayer.objects.filter(match_id=match)
    for player in registered_players:
        player.team = None
        player.save()
    messages.success(request, "Teams cleared")
    match.teams_allocated = False
    match.save()
    return HttpResponseRedirect(reverse('select_match'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def approve_member(request, pk):
    """Allows the manager to approve membership applications.
    Sets the is_approved property of the member to True
    and generates an email advising them they have been
    accepted"""
    member = ClubMember.objects.get(id=pk)
    member.is_approved = True
    member.save()
    messages.success(request, 'Application approved')
    send_mail('Application approved',
              'Congratulations! '
              'Your application to join RDFC has been approved.'
              'We look forward to seeing you!',
              'steve@rdfc.com',
              (member.email,))
    return HttpResponseRedirect(reverse('member_admin'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def reject_member(request, pk):
    """Allows the manager to reject membership applications
    and generates an email advising them they have been
    rejected"""
    queryset = ClubMember.objects.filter(is_approved=False)
    member = get_object_or_404(queryset, id=pk)
    messages.success(request, 'Application rejected')
    send_mail('Application rejected',
              'Sorry. Your application to join RDFC has not been approved'
              'Please contact steve@rdfc.com for further information',
              'steve@rdfc.com',
              (member.email,))
    member.delete()
    return HttpResponseRedirect(reverse('member_admin'))


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_member(request, pk):
    """Allows the manager to delete a member from the club
    database"""
    queryset = ClubMember.objects.filter(is_approved=True)
    member = get_object_or_404(queryset, id=pk)
    messages.success(request, 'Member deleted')
    member.delete()
    return HttpResponseRedirect(reverse('member_admin'))
