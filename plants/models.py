from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# from django.utils import timezone
from datetime import timedelta


class Plant(models.Model):
    name = models.CharField(max_length=100)
    days_to_harvest = models.IntegerField()
    estimated_yield_kg = models.FloatField()
    estimated_savings_usd = models.FloatField()
    date_planted = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def expected_harvest_date(self):
        return self.date_planted + timedelta(days=self.days_to_harvest)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
