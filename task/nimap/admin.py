from django.contrib import admin
from .models import Client,Project,User

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(User)