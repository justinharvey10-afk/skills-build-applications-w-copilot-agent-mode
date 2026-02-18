from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'display_name', 'weekly_goal', 'created_at')
	search_fields = ('display_name', 'user__username')
