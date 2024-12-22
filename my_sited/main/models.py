from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.username
# Create your models here.

class Habit(models.Model):
    user_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name