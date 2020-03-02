from django.db import models

# Create your models here.

class Restaurent_data(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Restaurent(models.Model):
    DAYS_CHOICES = (
        ("0", "0"), # Monday
        ("1", "1"), # Tuesday
        ("2", "2"), # Wednesday
        ("3", "3"), # Thursday
        ("4", "4"), # Friday
        ("5", "5"), # Saturday
        ("6", "6"), # Sunday
    )

    restaurent = models.ForeignKey(Restaurent_data, on_delete=models.CASCADE, blank=False, null=False)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    day = models.CharField(max_length=10, blank=False, null=False, choices=DAYS_CHOICES)

    def __str__(self):
        return self.restaurent.name + ' - ' + self.day

    def __unicode__(self):
        return self.restaurent.name + ' - ' + self.day
