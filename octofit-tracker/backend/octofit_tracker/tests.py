from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        Activity.objects.create(user=ironman, type='run', duration=30)
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', suggested_for_team=marvel)
        Leaderboard.objects.create(user=ironman, points=100)

    def test_user_team(self):
        user = User.objects.get(username='ironman')
        self.assertEqual(user.team.name, 'Marvel')

    def test_activity(self):
        activity = Activity.objects.get(type='run')
        self.assertEqual(activity.duration, 30)

    def test_leaderboard(self):
        entry = Leaderboard.objects.get(points=100)
        self.assertEqual(entry.user.username, 'ironman')
