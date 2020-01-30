from django.urls import path
from . import views

app_name = 'basic_app'
urlpatterns = [
    
    path('',views.other, name= 'other' ),
    path('help/', views.help, name='help')
]
