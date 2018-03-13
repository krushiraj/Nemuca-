from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Year = (("1","1"),("2","2"),("3","3"),("4","4"))


class SignupForm(UserCreationForm):
#    email = forms.EmailField(label='email', required=True)
#    year = forms.ChoiceField(choices=Year, widget = forms.RadioSelect(),required=True)
    class Meta:
        model = User
        fields = ('username')