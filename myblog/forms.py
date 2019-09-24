from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

        widget = {
            'title': forms.TextInput(attrs={'class': 'textinputclass', 'label':'Title1'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widget = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
############################################################################################
############################################################################################
