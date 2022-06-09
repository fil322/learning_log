from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
# from django.contrib.auth import login

urlpatterns = [
    # Страница входа
    # path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # Страница регистрации
    path('register/', views.register, name='register'),
    # Страница выхода
    path('logout/', views.logout_view, name='logout'),
]