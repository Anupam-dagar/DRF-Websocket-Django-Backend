from django.db import models

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
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    day = models.CharField(max_length=10, blank=False, null=False, choices=DAYS_CHOICES)

    def __str__(self):
        return self.restaurant.name + ' - ' + self.day

    def __unicode__(self):
        return self.restaurant.name + ' - ' + self.day
