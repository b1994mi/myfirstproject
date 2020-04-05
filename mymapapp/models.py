from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# A Model to log user log in/out activities. logb = True is a log in, False is a log out.
class Logger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logb = models.BooleanField()
    tlog = models.DateTimeField(auto_now=False, auto_now_add=False)

# The Profile Model (or table) is to extend the User Model, thus it has one to one field.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adrs = models.TextField("Address", max_length=500, blank=True)
    phon = models.BigIntegerField("Phone Number", blank=True, null=True)
    #This fields should be Point field using GEODjango, but I use decimal for simplicity sake.
    lngd = models.DecimalField("Longitude", max_digits=22, decimal_places=16, blank=True, null=True)
    latd = models.DecimalField("Latitude", max_digits=22, decimal_places=16, blank=True, null=True)

# Signals so Profile model will be created/updated when create/update User instances.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()