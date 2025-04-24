from django import forms
from django_password_eye.fields import PasswordEye
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name','bio','pfp', 'password1', 'password2')
        
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Bio', 'style': 'width: 300px;', 'class': 'form-control','max_length': 500}))
    password1 = PasswordEye(label= 'Password')
    password2 = PasswordEye(label= 'Password')



    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) > 500:
            raise forms.ValidationError("Bio cannot be more than 500 characters")
        return bio

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
       
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 300px;', 'class': 'form-control'}))
    password = PasswordEye(label= 'Password')


