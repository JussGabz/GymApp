import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Exercise(models.Model):
    exercise_name = models.CharField(max_length=50)
    target_area = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=20)
    date_added = models.DateTimeField("Date Added")

    def __str__(self):
        return self.exercise_name
    
    def recently_added_exercise(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)


