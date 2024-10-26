from rest_framework import serializers
from .models import User, Client, Project

class User_S(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class Client_S(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name','created_at']  

class Project_S(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    client = serializers.ReadOnlyField(source='client.name')  

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users','created_at']

    def to_representation(self, instance):
        """
        Customize the output format to match the desired response structure.
        """
        response = super().to_representation(instance)
        response['client'] = instance.client.client_name  
        response['users'] = [
            {'id': user.id, 'name': user.name} for user in instance.users.all()
        ]
        return response