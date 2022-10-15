from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/<str:type>', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/getPassword/', views.getPassword, name='getPassword'),
    path('home/', include('Home.urls')),
]