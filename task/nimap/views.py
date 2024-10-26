from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import generics
from .models import Client, Project
from .serializers import Client_S, Project_S, User_S
from .models import User
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class CreateUser(generics.ListCreateAPIView):  
    queryset = User.objects.all()
    serializer_class = User_S
    permission_classes = [AllowAny]

class UpdateDelUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = User_S


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            login(request, user)  
            return redirect('login')  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form}) 

class CustomLoginView(LoginView):
    template_name = 'login.html'  

    def get_success_url(self):
        return reverse_lazy('create-users') 

class CreateClients(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = Client_S


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.username) 

class UpdateDelClients(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = Client_S

class CreateProjects(generics.ListCreateAPIView):
    serializer_class = Project_S

    def perform_create(self, serializer):
        client_id = self.kwargs.get('id')
        client = Client.objects.get(id=client_id)  
        serializer.save(client=client)

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(users=user) 

class UpdateDelProjects(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = Project_S

class RegistrationView(TemplateView):
    template_name = 'register.html'