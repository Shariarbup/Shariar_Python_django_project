from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    
     path('', views.home, name='home' ),
     path('register/', views.register, name= 'register'),
     path('logout/', views.user_logout, name='logout'),
     path('special/', views.special, name='special'),
     path('user_login/',views.user_login, name='user_login'),


]
