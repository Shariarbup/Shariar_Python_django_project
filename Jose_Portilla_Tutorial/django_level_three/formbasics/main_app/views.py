from django.shortcuts import render
from main_app.forms import UserForm
# Create your views here.
def home(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Do Something Code
            print("Validation Success.")

            print('First name : '+form.cleaned_data['first_name'])
            print('Last Name : '+form.cleaned_data['last_name'])
            print('Email : '+form.cleaned_data['email'])
            print('Text : '+form.cleaned_data['text'])



    return render(request,'main_app/index.html', {'form': form})