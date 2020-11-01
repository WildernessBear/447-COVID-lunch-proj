from django import forms

from .models import MyUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'email')

