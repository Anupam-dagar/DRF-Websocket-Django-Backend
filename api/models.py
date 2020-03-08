from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Restaurant_names(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Restaurant(models.Model):
    DAYS_CHOICES = (
        ("0", "Monday"),
        ("1", "Tuesday"),
        ("2", "Wednesday"),
        ("3", "Thursday"),
        ("4", "Friday"),
        ("5", "Saturday"),
        ("6", "Sunday"),
    )

    restaurant = models.ForeignKey(Restaurant_names, on_delete=models.CASCADE, blank=False, null=False)
    opening_time = JSONField(default=dict)
    closing_time = JSONField(default=dict)

    def __str__(self):
        return self.restaurant.name + ' - ' + self.day

    def __unicode__(self):
        return self.restaurant.name + ' - ' + self.day
