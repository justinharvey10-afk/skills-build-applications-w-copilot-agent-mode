from rest_framework import viewsets


from .models import Profile, Team, Activity, Workout, Leaderboard
from .serializers import ProfileSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.select_related('user').all()
	serializer_class = ProfileSerializer


class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.select_related('user').all()
	serializer_class = ActivitySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.select_related('user').all()
	serializer_class = WorkoutSerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.select_related('user').all()
	serializer_class = LeaderboardSerializer
