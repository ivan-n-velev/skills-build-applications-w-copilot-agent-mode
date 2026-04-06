from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()

        # Clear all collections (order matters for FK constraints)
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (super heroes)
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        ironman.team = marvel
        ironman.save()

        captain = User.objects.create_user(username='captain_america', email='captain@marvel.com', password='password')
        captain.team = marvel
        captain.save()

        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        batman.team = dc
        batman.save()

        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')
        superman.team = dc
        superman.save()

        # Create Activities
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=captain, type='cycle', duration=45)
        Activity.objects.create(user=batman, type='swim', duration=60)
        Activity.objects.create(user=superman, type='run', duration=50)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all Marvel heroes', suggested_for_team=marvel)
        Workout.objects.create(name='Strength Training', description='Strength for DC heroes', suggested_for_team=dc)

        # Create Leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=captain, points=90)
        Leaderboard.objects.create(user=batman, points=95)
        Leaderboard.objects.create(user=superman, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
