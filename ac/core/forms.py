from django import forms
from django.contrib.auth.forms import UserCreationForm, EmailField
from django.contrib.auth.models import User

#from verified_email_field.forms import VerifiedEmailField,EmailField


class SignupForm(UserCreationForm):
    email = EmailField(label='email', required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')