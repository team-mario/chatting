from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=25)
    password = forms.CharField(label='password 1', max_length=25)
    checkPassword = forms.CharField(label='password 2', max_length=25)