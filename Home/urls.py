from django.urls import path
from . import views
urlpatterns = [
    path('userHome/', views.userHome, name='userHome'),
    path('loginUser/', views.loginUser, name='loginUser'),
]
