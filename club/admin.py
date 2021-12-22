from django.contrib import admin
from .models import Member, Team, Match

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
	list_filter = ('is_approved', 'is_available')
	list_display = ('first_name', 'last_name', 'points', 'is_available')


admin.site.register(Member, MemberAdmin)
admin.site.register(Team)
admin.site.register(Match)
