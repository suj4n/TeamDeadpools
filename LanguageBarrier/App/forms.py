from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'para']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the post title'}),
            'para': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the post content'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'para']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the post title'}),
            'para': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the post content'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('This field is required')
        return title

    def clean_para(self):
        para = self.cleaned_data.get('para')
        if not para:
            raise forms.ValidationError('This field is required')
        return para