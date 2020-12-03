from django import forms

from .models import MyUser, Student


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'email')

class DietaryForm(forms.ModelForm):
    milk = forms.BooleanField(required=False)
    eggs = forms.BooleanField(required=False)
    fish = forms.BooleanField(required=False)
    shellfish = forms.BooleanField(required=False)
    tree_nuts = forms.BooleanField(required=False)
    peanuts = forms.BooleanField(required=False)
    wheat = forms.BooleanField(required=False)
    soybeans = forms.BooleanField(required=False)
    # what's a good text field?
    other = forms.CharField(required=False)

    class Meta:
        model = Student
        fields =('milk', 'eggs', 'fish', 'shellfish', 'tree_nuts', 'peanuts', 'wheat', 'soybeans', 'other')
