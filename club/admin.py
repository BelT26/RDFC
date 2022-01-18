from django.contrib import admin
from .models import  Team, Match, ClubMember


# Register your models here.
@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):

    list_filter = ('is_approved', 'is_available')
    list_display = ('first_name', 'last_name', 'points', 'is_available')
    search_fields = ['first_name', 'last_name','username']
    actions = ['approve_member']

    def approve_member(self, request, queryset):
        queryset.update(is_approved=True)


admin.site.register(Team)
admin.site.register(Match)
admin.site.register(MatchPlayer)
admin.site.regiter(Result)
