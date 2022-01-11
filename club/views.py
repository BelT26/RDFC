from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ClubMember, Match
#from .forms import SignUpForm, LogInForm

# Create your views here.


def index(request):
    return render(request, 'club/index.html')


available_players = []
reserves = []
blues = []
whites = []

def members(request):
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
    return render(request, 'club/management.html')


def applications(request):
    return render(request, 'club/applications.html')


def add_fixture(request):
    return render(request, 'club/fixture.html')


def add_result(request):
    return render(request, 'club/result.html')


def registrations(request):
    return render(request, 'club/registrations.html')


# def mysignup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             member = Member(
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']
#             )
#             member.save()
#             return HttpResponseRedirect('/thankyou')
#     else:        
#         form = SignUpForm()
        
#     return render(request, 'club/signup.html', {
#         'form': form
#     })


def thankyou(request):
    return render(request, 'club/thankyou.html')


# def mylogin(request):
#     if request.method == 'POST':
#         form = LogInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             approved_members = Member.objects.all().filter(is_approved=True)
#             while password_attempts < 3:
#             for member in approved_members:
#                 if member['username'] == username:
#                     member_logging_in = member
#                     password_attempts_remaining = 3
#                     while password_attempts > 0
#                     if member_logging_in['password'] == password:
#                           member_logging_in['is_logged_in'] == True
#                           messages.success(request, 'You have successfully logged in') 
#                           return HttpResponseRedirect(reverse('members')
#                     else: 
#                         password_attempts_remaining -= 1
                             
#                         messages.error(request, f"Incorrect password. {password_attempts_remaining} attempts remaining )
#                 else:
#                     messages.error(request, 'Sorry no member is registered with that username')
#                     form = LogInForm()
#                     
            
#     form = LogInForm()
#     return render(request, 'club/login.html', {
#         'form': form
#     })




def book_match_place(request):
    player = None
    if request.user.is_authenticated():
        player = request.user
        if len(available_players) <= 12:  
            player['is_in_team'] = True
            available_players.append(player)
            messages.success(request, 'You have been allocated a place in the next match!')
        else:
            reserves.append(player)
            messages.warning(request, 'Unfortunately there is no room on the team')
            messages.warning(request, f'You are number {len(reserves)} on the reserve list')
    return HttpResponseRedirect(reverse('members'))
