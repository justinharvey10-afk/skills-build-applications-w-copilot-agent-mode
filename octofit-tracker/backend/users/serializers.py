from rest_framework import serializers

from .models import Profile


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