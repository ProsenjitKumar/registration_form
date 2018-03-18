from django.contrib.auth.forms import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Enter Your Username'}
    ), required=True, max_length=60)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}
    ), required=True, max_length=60)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}
    ), required=True, max_length=60)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}
    ), required=True, max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}
    ), required=True, max_length=60)
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}
    ), required=True, max_length=60)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']