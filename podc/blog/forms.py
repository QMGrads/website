from django import forms

from .models import Article

class PostForm(forms.ModelForm):
    class Meta:
	    model = Article
	    fields = ('title', 'author', 'article_title', 'article_image')