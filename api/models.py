from django.db import models
from django.contrib.auth.models import User
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
        return self.restaurant.name

    def __unicode__(self):
        return self.restaurant.name

class UserCollections(models.Model):
    # A collection created by a user
    name = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        unique_together = ('name', 'user',)

    def __str__(self):
        return self.user.username + ' - ' + self.name

    def __unicode__(self):
        return self.user.username + ' - ' + self.name

class RestaurantCollections(models.Model):
    # All collections of restaurants by a user
    restaurant_collection = models.ForeignKey(UserCollections, on_delete=models.CASCADE, blank=False, null=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.restaurant_collection.name + ' - ' + self.restaurant_collection.user.username

    def __unicode__(self):
        return self.restaurant_collection.name + ' - ' + self.restaurant_collection.user.username

class Collections(models.Model):
    user_collections = models.ForeignKey(UserCollections, on_delete=models.CASCADE, blank=False, null=False)
    collaborators = models.ManyToManyField(User)

    def __str__(self):
        return self.user_collections.name + ' - ' + self.user_collections.user.username

    def __unicode__(self):
        return self.user_collections.name + ' - ' + self.user_collections.user.username
