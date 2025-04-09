from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    # ...other fields...

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    # ...other fields...

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ...other fields...

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # ...other fields...

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ...other fields...
