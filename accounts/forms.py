from django import forms
from .models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(30),
        ]
    )
    class Meta:
        model = User
        forms = ['login', 'password']