from django.shortcuts import render
from main_app.forms import UserNewForm
# Create your views here.

def index(request):
    form = UserNewForm()
    if request.method == 'POST':
        form = UserNewForm(request.POST)
        if form.is_valid():
            form.save(commit= True)
            
        else:
            print('Error invalid')
    return render(request,'main_app/index.html', {'form': form})