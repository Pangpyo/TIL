from django import forms
from .models import Movies


# ModelForm class 생성
class MoiveForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ["title", "summary", "running_time"]
