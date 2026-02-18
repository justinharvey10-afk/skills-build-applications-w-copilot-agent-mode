
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Profile, Team, Activity, Workout, Leaderboard
from .serializers import ProfileSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer, UserSerializer

# UserViewSet for /api/users/
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


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
