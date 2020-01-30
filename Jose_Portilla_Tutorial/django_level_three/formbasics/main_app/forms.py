from django import forms
from django.core import validators

# Custom validators
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Need to start with the first name with z')

class UserForm(forms.Form):
    first_name = forms.CharField(validators= [check_for_z])
    last_name =  forms.CharField()
    email = forms.EmailField()
    veryfy_email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required= False, widget= forms.HiddenInput,
                                                        validators= [validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['veryfy_email']
        if email != vmail:
            raise forms.ValidationError('Email dont match check again')

    # Manually craete validation
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotcha a bot!!')
    #     return botcatcher