from django import forms
from blog import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','description','picture','location']
        