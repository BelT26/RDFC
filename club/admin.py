from django.contrib import admin
from .models import  Team, Match, ClubMember, MatchPlayer, Result


# Register your models here.
@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):

    list_filter = ('is_approved', 'is_available')
    list_display = ('first_name', 'last_name', 'points', 'is_available')
    search_fields = ['first_name', 'last_name','username']
    actions = ['approve_member']

    def approve_member(self, request, queryset):
        queryset.update(is_approved=True)


@admin.register(MatchPlayer)
class MatchPlayerAdmin(admin.ModelAdmin):

    list_filter = ('team', 'reserve')
    list_display = ('player_id', 'match_id', 'team')
    search_fields = ['player_id']
    


admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Result)
