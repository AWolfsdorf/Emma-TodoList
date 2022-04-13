from django import forms
from users.models import UserProfile
from django.contrib.auth import password_validation
from django.utils.translation import gettext, gettext_lazy as _


class UserRegisterForm (forms.ModelForm):
    email = forms.EmailField(
        label=_("email").capitalize,
        widget=forms.EmailInput(),
        help_text=_("A valid email address, please.")
    )

    name = forms.CharField(
        label=_("username").capitalize,
        strip=False,
        widget=forms.TextInput()
    )

    password = forms.CharField(
        label=_("Password").capitalize,
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),

    )
    
    class Meta:
        model = UserProfile
        fields = ['name','email','password']

        

class UserLoginForm (forms.ModelForm):
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput()
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = UserProfile
        fields = ['email','password']

        