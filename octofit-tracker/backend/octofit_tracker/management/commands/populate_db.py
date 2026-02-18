from django.core.management.base import BaseCommand
from users.models import Profile
from django.contrib.auth.models import User
from djongo import models as djongo_models
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for non-ORM collections
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create teams
        marvel_id = db.teams.insert_one({'name': 'Team Marvel'}).inserted_id
        dc_id = db.teams.insert_one({'name': 'Team DC'}).inserted_id

        # Create users (superheroes)
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team_id': marvel_id, 'display_name': 'Iron Man'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team_id': marvel_id, 'display_name': 'Captain America'},
            {'username': 'batman', 'email': 'batman@dc.com', 'team_id': dc_id, 'display_name': 'Batman'},
            {'username': 'superman', 'email': 'superman@dc.com', 'team_id': dc_id, 'display_name': 'Superman'},
        ]
        user_ids = []
        for u in users:
            user_obj = User.objects.create_user(username=u['username'], email=u['email'], password='password')
            Profile.objects.create(user=user_obj, display_name=u['display_name'])
            user_doc = {'username': u['username'], 'email': u['email'], 'team_id': u['team_id'], 'display_name': u['display_name']}
            user_ids.append(db.users.insert_one(user_doc).inserted_id)

        # Create activities
        activities = [
            {'user_id': user_ids[0], 'type': 'run', 'distance': 5, 'duration': 30},
            {'user_id': user_ids[1], 'type': 'cycle', 'distance': 20, 'duration': 60},
            {'user_id': user_ids[2], 'type': 'swim', 'distance': 2, 'duration': 40},
            {'user_id': user_ids[3], 'type': 'run', 'distance': 10, 'duration': 50},
        ]
        db.activities.insert_many(activities)

        # Create workouts
        workouts = [
            {'user_id': user_ids[0], 'name': 'Chest Day', 'exercises': ['bench press', 'push ups']},
            {'user_id': user_ids[1], 'name': 'Leg Day', 'exercises': ['squats', 'lunges']},
            {'user_id': user_ids[2], 'name': 'Cardio', 'exercises': ['treadmill', 'cycling']},
            {'user_id': user_ids[3], 'name': 'Strength', 'exercises': ['deadlift', 'pull ups']},
        ]
        db.workouts.insert_many(workouts)

        # Create leaderboard
        leaderboard = [
            {'user_id': user_ids[0], 'points': 100},
            {'user_id': user_ids[1], 'points': 90},
            {'user_id': user_ids[2], 'points': 110},
            {'user_id': user_ids[3], 'points': 95},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Ensure unique index on email
        db.users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
