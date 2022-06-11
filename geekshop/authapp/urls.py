from django.urls import path
import authapp.views as authapp

app_name = 'autapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
    path('logout/', authapp.logout, name='logout'),
]
