from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


User = settings.AUTH_USER_MODEL

class CustomerProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        CustomerProfile.objects.get_or_create(user=instance)

post_save.connect(user_created_receiver, sender=User)