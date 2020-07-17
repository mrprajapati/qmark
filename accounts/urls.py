from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
