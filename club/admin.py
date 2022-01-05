from django.contrib import admin
from .models import Member, Team, Match

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

	list_filter = ('is_approved', 'is_available')
	list_display = ('first_name', 'last_name', 'points', 'is_available')
	search_fields = ['first_name', 'last_name']


admin.site.register(Team)
admin.site.register(Match)
