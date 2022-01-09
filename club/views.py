from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Member, Match
from .forms import SignUpForm, LogInForm

# Create your views here.


def index(request):
    return render(request, 'club/index.html')


available_players = ['a', 'a', 'b', 'a', 'a', 'b', 'a', 'a', 'b', 'a', 'a', 'b']
blues = []
whites = []

def members(request):
    league_table = Member.objects.all().order_by('-points')
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


def social(request):
    return render(request, 'club/social.html')


def management(request):
    return render(request, 'club/management.html')


def mysignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            member = Member(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            member.save()
            return HttpResponseRedirect('/thankyou')
    else:        
        form = SignUpForm()
        
    return render(request, 'club/signup.html', {
        'form': form
    })


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
#                     password_attempts = 0
#                     if member_logging_in['password'] == password:
#                         member_logging_in['is_logged_in'] == True
#                         return 
#                     else: 
#                         print('incorrect password')
#                         password_attempts += 1
#                         # return render(request, 'club/incorrect_password.html')
#                 else:
#                     print('no member with that username')
#                     # return render(request, 'club/no_user.html')
            
#     form = LogInForm()
#     return render(request, 'club/login.html', {
#         'form': form
#     })




def book_match_place(player):
    if len(available_players) < 12:
        player['is_in_team'] = True
        available_players.append(player)
        print('Your place on the team has been booked')      
    else:
        reserves.append(player)
        print('Unfortunately there is no room on the team')
        print(f'You are number {len(reserves)} on the reserve list')