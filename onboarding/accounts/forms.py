
from .models import *
from django import forms
from django.contrib.auth import authenticate

User = Account


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['Email', 'First_name', 'Last_name', 'Sex', 'password']


class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('this user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('incorrect password')
            if not user.is_active:
                raise forms.ValidationError('this user is not active')
        return super(LoginForm, self).clean(*args, **kwargs)
