from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class MateRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = ''
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = ''
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Pasword confirmation'
        self.fields['password2'].help_text = ''

class MateAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = ''
        self.fields['password'].label = ''
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].help_text = ''