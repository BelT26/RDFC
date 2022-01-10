from django.contrib import admin
from .models import  Team, Match, Member, ClubMember


# Register your models here.
@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):

    list_filter = ('is_approved', 'is_available')
    list_display = ('first_name', 'last_name', 'points', 'is_available')
    search_fields = ['first_name', 'last_name']
    actions = ['approve_member']

    def approve_member(self, request, queryset):
        queryset.update(is_approved=True)


admin.site.register(Team)
admin.site.register(Match)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    list_filter = ('is_approved', 'is_available')
    list_display = ('first_name', 'last_name', 'points', 'is_available')
    search_fields = ['first_name', 'last_name']
    actions = ['approve_member']

    def approve_member(self, request, queryset):
        queryset.update(is_approved=True)
