# application forms
from django import forms


class RegFormAlpha(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    gender = forms.CharField(label='Your name', max_length=100)
    country = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your name', max_length=100)


class RegFormBeta(forms.Form):
    web_url = forms.CharField(label='Your name', max_length=100)
    about = forms.CharField(label='Your name', max_length=100)
    skills = forms.CharField(label='Your name', max_length=100)


class RegFormGama(forms.Form):
    avatar = forms.FileField(label='Select your photo')


class RegFormOmga(forms.Form):
    cover_photo = forms.FileField(label='Select your photo')


class LoginForm(forms.Form):
    email = forms.CharField(label='Enter your email.')
    password = forms.CharField(label='Enter your password.')
