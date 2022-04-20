from django.db import models


# Create your models here.

class user(models.Model):
    email = models .CharField(max_length=255)
    first_name = models .CharField(max_length=255)
    last_name = models .CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='media/',blank=True,null=True)
    is_verified = models.BooleanField()
    auth_provided = models.CharField(max_length=100,blank=True,null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.first_name
