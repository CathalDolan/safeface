from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


# User Profile for storing delivery address
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=254,
                                 null=True,
                                 blank=True)
    default_email = models.EmailField(null=True,
                                      blank=True)
    default_phone_number = models.CharField(max_length=20,
                                            null=True,
                                            blank=True)
    default_company_name = models.CharField(max_length=254,
                                            null=True,
                                            blank=True)
    default_department = models.CharField(max_length=25,
                                          null=True,
                                          blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True,
                                               blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True,
                                            blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True,
                                      blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True,
                                        blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


# Create a new profile for anyone who signs up or update an existing one
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: save the profile
    instance.userprofile.save()
