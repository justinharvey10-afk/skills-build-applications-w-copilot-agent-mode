
from rest_framework import serializers
from django.contrib.auth.models import User

# User serializer for /api/users/
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

from .models import Profile

from .models import Team, Activity, Workout, Leaderboard


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'display_name', 'bio', 'weekly_goal', 'created_at']

    def get_id(self, obj):
        return str(obj.id)

    def get_user_id(self, obj):
        return str(obj.user_id)


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['id', 'name', 'created_at']

    def get_id(self, obj):
        return str(obj.id)


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'type', 'distance', 'duration', 'created_at']

    def get_id(self, obj):
        return str(obj.id)

    def get_user_id(self, obj):
        return str(obj.user_id)


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'user_id', 'name', 'exercises', 'created_at']

    def get_id(self, obj):
        return str(obj.id)

    def get_user_id(self, obj):
        return str(obj.user_id)


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'points', 'created_at']

    def get_id(self, obj):
        return str(obj.id)

    def get_user_id(self, obj):
        return str(obj.user_id)