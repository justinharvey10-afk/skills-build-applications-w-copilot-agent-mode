from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	display_name = models.CharField(max_length=100)
	bio = models.TextField(blank=True)
	weekly_goal = models.PositiveIntegerField(default=3)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.display_name


class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
	type = models.CharField(max_length=50)
	distance = models.FloatField()
	duration = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.type}"


class Workout(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
	name = models.CharField(max_length=100)
	exercises = models.JSONField(default=list)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.name}"


class Leaderboard(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
	points = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.points} pts"
