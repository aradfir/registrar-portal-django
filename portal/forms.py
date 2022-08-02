from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import MinValueValidator, MaxValueValidator


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

        error_messages = {
            'username': {
                "unique": "A user with that username already exists. CUSTOM!",

            }
        }

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password and Password Repeat do not match! CUSTOM")
        return cleaned_data

    def save(self, commit=True):
        super(RegisterForm, self).save(commit)
        u = User.objects.get(username=self.cleaned_data.get('username'))
        u.set_password(self.cleaned_data.get('password'))
        u.save()
        return u


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


class ContactForm(forms.Form):
    title = forms.CharField(max_length=150)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea, validators=[MinValueValidator(10, 'Message Too Short!'),
                                                              MaxValueValidator(250, "Message Too Long!")])
