from django.contrib import admin
from .models import Member, Team, Match

# Register your models here.
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Match)
