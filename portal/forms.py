from django import forms
# from django.contrib.auth.models import User

from .models import Course, UserProfile
from django.contrib.auth import authenticate
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import Group

prof_group, created = Group.objects.get_or_create(name='Professor')
std_group, created = Group.objects.get_or_create(name='Student')


class SettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'first_name', 'last_name', 'gender', 'bio')

    def clean(self):
        super(SettingsForm, self).clean()
        if self.cleaned_data.get('last_name') == '':
            self.cleaned_data.pop('last_name')
        if self.cleaned_data.get('first_name') == '':
            self.cleaned_data.pop('first_name')
        return self.cleaned_data


class CourseCreateForm(forms.ModelForm):
    # day_1 = forms.IntegerField(choices=Course.DAYS_OF_WEEK, required=True)
    # day_2 = forms.IntegerField(required=False, choices=Course.DAYS_OF_WEEK)

    class Meta:
        model = Course
        fields = '__all__'


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    account_type = forms.ChoiceField(choices=((prof_group.id, 'Professor'), (std_group.id, 'Student')))

    class Meta:
        model = UserProfile
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
        u = UserProfile.objects.get(username=self.cleaned_data.get('username'))
        u.set_password(self.cleaned_data.get('password'))
        u.save()
        u.groups.add(self.cleaned_data.get('account_type'))
        print(u.groups.get())
        return u


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())


class ContactForm(forms.Form):
    form_title = forms.CharField(max_length=150, label="Title")
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea, validators=[MinLengthValidator(10, 'Message Too Short!'),
                                                              MaxLengthValidator(250, "Message Too Long!")])
