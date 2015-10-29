from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$',
                                widget=forms.TextInput(attrs=dict(
                                    required=True,
                                    max_length=30)),
                                label=_("Username"),
                                error_messages={'invalid': ("This value must"
                                                            "contain "
                                                            "only letters,"
                                                            "numbers and"
                                                            "underscores.")})
    email = forms.EmailField(widget=forms.TextInput(
        attrs=dict(required=True,
                   max_length=30)),
        label=_("Email address"))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(
            required=True,
            max_length=30,
            render_value=False)),
        label=_("Password"))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True,
                   max_length=30,
                   render_value=False)),
        label=_("Password (again)"))

    def clean_username(self):
        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists."
                                      "Please try another one."))

    def clean(self):
        cleaned_value = self.cleaned_data
        if 'password1' in cleaned_value and 'password2' in cleaned_value:
            if cleaned_value['password1'] != cleaned_value['password2']:
                raise forms.ValidationError(_("The two password fields"
                                              "did not match."))
        return cleaned_value
