from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title', 'description', 'image']
    
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;', 'class': 'form-control'}))
    
	description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description', 'style': 'width: 300px;', 'class': 'form-control'}))

