from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	title = forms.CharField(label='title',
	widget=forms.TextInput(attrs={'placeholder': 'Title of Your Story...'}))
	content = forms.CharField(label='title',
	widget=forms.Textarea(attrs={'placeholder': 'Start Writing...'}))
	tags = forms.CharField()

	class Meta:
		model = Post
		fields =('title','content','tags') 