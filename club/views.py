from django.shortcuts import render
from .models import Member

# Create your views here.


def index(request):
    return render(request, 'club/index.html')


def members(request):
    return render(request, 'club/members.html')
