
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .validators import validate_mobile_number, validate_password
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _
from django.conf import settings


#class User(AbstractUser):
    

    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, blank=True, default='')
    user_type = models.CharField(max_length=20, blank=True, default='')


    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.user.username
    


