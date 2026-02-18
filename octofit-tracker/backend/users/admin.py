from django.contrib import admin


from .models import Profile, Team, Activity, Workout, Leaderboard


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'display_name', 'weekly_goal', 'created_at')
	search_fields = ('display_name', 'user__username')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'created_at')
	search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'type', 'distance', 'duration', 'created_at')
	search_fields = ('user__username', 'type')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'name', 'created_at')
	search_fields = ('user__username', 'name')


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'points', 'created_at')
	search_fields = ('user__username',)
