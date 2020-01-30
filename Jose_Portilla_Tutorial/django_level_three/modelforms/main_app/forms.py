from main_app.models import UserForm
from django import forms
class UserNewForm(forms.ModelForm):
    class Meta():
        model = UserForm
        fields = '__all__'