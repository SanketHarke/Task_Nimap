from django.urls import path
from .views import CreateClients,UpdateDelClients,CreateProjects,UpdateDelProjects,CreateUser,UpdateDelUser,register
from django.contrib.auth import views as auth_views

class CustomLoginView(auth_views.LoginView):
    def get_success_url(self):
        return '/clients/'
    

urlpatterns = [
    path('clients/', CreateClients.as_view(), name='create-clients'),
    path('clients/<int:pk>/', UpdateDelClients.as_view(), name='update-delete-clients'),
    path('clients/<int:id>/projects/', CreateProjects.as_view(), name='create-projects'),
    path('projects/<int:pk>/', UpdateDelProjects.as_view(), name='update-delete-projects'),
    path('users/', CreateUser.as_view(), name='create-users'),
    path('users/<int:pk>/', UpdateDelUser.as_view(), name='update-delete-users'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
]