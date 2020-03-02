from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    gender = models.TextField(max_length=10)
    country = models.TextField(max_length=80)
    web_url = models.TextField(max_length=80)
    about = models.TextField(max_length=80)
    skills = models.TextField(max_length=80)
    avatar = models.TextField(max_length=100)
    cover_photo = models.TextField(max_length=100)

# @receiver(post_save, sender=User)
# def create_user_instance(sender, instance, created, **kwargs):
#     if created:
#         UserDetails.object.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_instance(sender, instance, **kwargs):
#     instance.profile.save()

