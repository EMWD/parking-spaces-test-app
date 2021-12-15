from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import *
from icecream import ic
from .helpers import AccessResolver


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))

    CHOICES = ((1, 'Менеджер'), (0, 'Работник'),)
    is_stuff = forms.CharField(widget=forms.Select(choices=CHOICES))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_stuff')

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.is_staff = self.cleaned_data['is_stuff']
        if commit:
            user.save()
        return user


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = "Автор не указан"
        self.fields['status'].empty_label = "Publish"

    title = forms.CharField(
        label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))

    text = forms.CharField(
        label='Примечание', widget=forms.Textarea(attrs={'class': 'input-text-area'}))

    class Meta:
        model = Task
        fields = ('title', 'text', 'author', 'status',
                  'slug', 'parking_lot_number')

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Слишком длинное описание(>200 символов)')

        return title

class MyForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'author', 'status',
                  'slug', 'parking_lot_number')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # capatcha = CaptchaField()
