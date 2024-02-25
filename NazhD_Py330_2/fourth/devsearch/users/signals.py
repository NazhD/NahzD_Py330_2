from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User


def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
    # print("Profile Saved!")
    # print("Sender:", sender)
    # print("instance", instance)
    # print("created", created)


def delite_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=Profile)
post_delete.connect(delite_user, sender=Profile)