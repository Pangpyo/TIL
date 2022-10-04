from django import forms
from .models import Article


# ModelForm class 생성
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
