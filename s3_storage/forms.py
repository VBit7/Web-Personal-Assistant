from django import forms
from .models import S3File

class S3FileForm(forms.ModelForm):
    class Meta:
        model = S3File
        fields = ['file', 'category']
