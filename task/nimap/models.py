from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    name = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    location_city = models.CharField(max_length=255, null=True, blank=True)  
    
    class Meta:
        db_table = 'custom_user'

    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_user_permissions')

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    created_by = models.CharField(max_length=255)
   
class Project(models.Model):
    project_name = models.CharField(max_length=255)  
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name        