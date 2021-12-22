from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Member, Match
from .forms import SignUpForm

# Create your views here.


def index(request):
    return render(request, 'club/index.html')


def members(request):
    league_table = Member.objects.all().order_by('-points')
    next_fixture = Match.objects.all().order_by('-match_date')[0]
    all_matches = Match.objects.all().order_by('-match_date')
    past_results = all_matches[1:]
    context = {
        'league_table': league_table,
        'next_fixture': next_fixture,
        'past_results': past_results
    }
    return render(request, 'club/members.html', context)


def social(request):
    return render(request, 'club/social.html')


def signup(request):
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
