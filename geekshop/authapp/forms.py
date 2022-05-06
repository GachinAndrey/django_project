from django import forms
from django.forms import ValidationError
from dataclasses import dataclass, fields
from pyexpat import model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import ShopUser


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ("username",)

class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'city',)

    def clean_age(self):
        if self.cleaned_data['age'] < 18 :
            #raise forms.ValidationError("Вы ещё не достигли 18 лет!")

        return self.cleaned_data