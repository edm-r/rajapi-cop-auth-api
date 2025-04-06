from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', "ADMIN"),
        ('member', "MEMBER"),
        ('mentor', "MENTOR"),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    newsletter_subscription = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username    
    