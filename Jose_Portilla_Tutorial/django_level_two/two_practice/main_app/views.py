from django.shortcuts import render
from main_app.models import User_s
# Create your views here.
def about(request):
    users = User_s.objects.all()
    user_dict ={'user_key': users}
    return render(request,'main_app/index.html', context = user_dict)
def home(request):
    return render(request, 'main_app/about.html')
