from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView, name='signup'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
   
]
